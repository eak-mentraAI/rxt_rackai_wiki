#!/usr/bin/env python3
"""
Erebine inference benchmark harness — validation val-erebine-inference-claims.

Tests the client-observable claims E-2..E-5 from
04-evidence/validations/Validate Erebine Inference Claims.md against a live
Erebine OpenAI-compatible endpoint (slug-routed).

Credentials come from the environment (never hardcode / commit a key):
  EREBINE_BASE   e.g. https://api.erebine.ai/proj_XXXX
  EREBINE_KEY    bearer token (ere_...)
  EREBINE_SLUG   endpoint slug, e.g. "ed"
  EREBINE_MODEL  model name for the body, e.g. "Qwen3.8-27B"

Usage:
  EREBINE_BASE=... EREBINE_KEY=... EREBINE_SLUG=ed EREBINE_MODEL=Qwen3.8-27B \
    python3 scripts/erebine-benchmark.py [--iters 30] [--json out.json]

stdlib only. Prints a markdown summary to stdout; optional --json dumps raw records.
"""
import argparse
import json
import os
import statistics
import sys
import time
import urllib.request
import urllib.error

BASE = os.environ.get("EREBINE_BASE", "").rstrip("/")
KEY = os.environ.get("EREBINE_KEY", "")
SLUG = os.environ.get("EREBINE_SLUG", "ed")
MODEL = os.environ.get("EREBINE_MODEL", "Qwen3.8-27B")


def _endpoint():
    return f"{BASE}/{SLUG}/v1/chat/completions"


def _headers(stream=False):
    h = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    }
    h["Accept"] = "text/event-stream" if stream else "application/json"
    return h


def _post(body, stream=False, timeout=60):
    data = json.dumps(body).encode()
    req = urllib.request.Request(_endpoint(), data=data, headers=_headers(stream))
    return urllib.request.urlopen(req, timeout=timeout)


def one_completion(messages, max_tokens):
    """Non-streaming call. Returns (elapsed_s, usage_dict, headers)."""
    body = {"model": MODEL, "messages": messages, "max_tokens": max_tokens}
    t0 = time.time()
    with _post(body, stream=False) as r:
        payload = json.loads(r.read().decode())
        hdrs = {k.lower(): v for k, v in r.getheaders()}
    return time.time() - t0, payload.get("usage", {}), hdrs


def one_stream(messages, max_tokens):
    """Streaming call. Returns (ttft_s, total_s, n_chunks)."""
    body = {"model": MODEL, "messages": messages, "max_tokens": max_tokens, "stream": True}
    t0 = time.time()
    first = None
    n = 0
    last = t0
    with _post(body, stream=True) as r:
        for raw in r:
            line = raw.decode().strip()
            if line.startswith("data:") and "[DONE]" not in line:
                if first is None:
                    first = time.time() - t0
                n += 1
                last = time.time()
    return (first if first is not None else float("nan")), (last - t0), n


def pct(xs, p):
    if not xs:
        return float("nan")
    xs = sorted(xs)
    k = (len(xs) - 1) * p / 100.0
    lo = int(k)
    hi = min(lo + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (k - lo)


def e3_e4_latency(iters, max_tokens):
    """E-3 TTFT (client proxy) + E-4 decode throughput via streaming."""
    ttfts, tps, wall = [], [], []
    for _ in range(iters):
        msgs = [{"role": "user", "content": "Write one sentence about the ocean."}]
        try:
            ttft, total, n = one_stream(msgs, max_tokens)
        except urllib.error.HTTPError as e:
            print(f"  [warn] stream HTTP {e.code}: {e.read()[:120]}", file=sys.stderr)
            continue
        if n == 0:
            continue
        ttfts.append(ttft)
        wall.append(total)
        decode = max(total - ttft, 1e-6)
        tps.append(n / decode)
        time.sleep(0.2)
    return {
        "n": len(ttfts),
        "ttft_ms_p50": pct(ttfts, 50) * 1000,
        "ttft_ms_p95": pct(ttfts, 95) * 1000,
        "ttft_ms_p99": pct(ttfts, 99) * 1000,
        "decode_chunks_per_s_median": statistics.median(tps) if tps else float("nan"),
        "wall_s_median": statistics.median(wall) if wall else float("nan"),
    }


def e2_prefix_cache(reps, prefix_tokens_approx):
    """E-2: repeat a shared long prefix, watch cached_tokens climb."""
    prefix = "The quick brown fox jumps over the lazy dog. " * prefix_tokens_approx
    records = []
    for i in range(reps):
        msgs = [{"role": "user", "content": prefix + f" Reply with the number {i}."}]
        try:
            _, usage, _ = one_completion(msgs, max_tokens=4)
        except urllib.error.HTTPError as e:
            print(f"  [warn] cache HTTP {e.code}: {e.read()[:120]}", file=sys.stderr)
            continue
        records.append({
            "rep": i,
            "prompt_tokens": usage.get("prompt_tokens"),
            "cached_tokens": (usage.get("prompt_tokens_details") or {}).get("cached_tokens"),
        })
        time.sleep(0.3)
    cold = records[0]["cached_tokens"] if records else None
    warm_max = max((r["cached_tokens"] or 0) for r in records) if records else None
    return {"records": records, "cold_cached": cold, "warm_max_cached": warm_max,
            "cache_active": bool(warm_max and warm_max > (cold or 0))}


def e5_erepress():
    """E-5: report the X-Erepress header on a normal request. Toggling requires
    the owner-gated MCP erepress.set tool, done out-of-band; here we record the
    header the router returns so the doc can note whether erepress is in-path."""
    msgs = [{"role": "user", "content": "Summarize: the sky is blue because of Rayleigh scattering."}]
    try:
        _, usage, hdrs = one_completion(msgs, max_tokens=16)
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}"}
    return {
        "x_erepress": hdrs.get("x-erepress"),
        "routed_model": hdrs.get("x-erebine-routed-model"),
        "routed_endpoint": hdrs.get("x-erebine-routed-endpoint"),
        "worker_id": hdrs.get("x-erebine-worker-id"),
        "prompt_tokens": usage.get("prompt_tokens"),
    }


def main():
    if not BASE or not KEY:
        print("ERROR: set EREBINE_BASE and EREBINE_KEY in the environment.", file=sys.stderr)
        sys.exit(2)
    ap = argparse.ArgumentParser()
    ap.add_argument("--iters", type=int, default=30, help="latency iterations (E-3/E-4)")
    ap.add_argument("--cache-reps", type=int, default=6)
    ap.add_argument("--max-tokens", type=int, default=64)
    ap.add_argument("--json", type=str, default="")
    args = ap.parse_args()

    print(f"# Erebine benchmark run", file=sys.stderr)
    print(f"endpoint={_endpoint()} model={MODEL}", file=sys.stderr)

    results = {
        "meta": {
            "endpoint": _endpoint(), "model": MODEL, "slug": SLUG,
            "iters": args.iters, "max_tokens": args.max_tokens,
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
    }
    print("running E-3/E-4 latency ...", file=sys.stderr)
    results["latency"] = e3_e4_latency(args.iters, args.max_tokens)
    print("running E-2 prefix cache ...", file=sys.stderr)
    results["prefix_cache"] = e2_prefix_cache(args.cache_reps, 60)
    print("running E-5 erepress header ...", file=sys.stderr)
    results["erepress"] = e5_erepress()

    if args.json:
        with open(args.json, "w") as f:
            json.dump(results, f, indent=2)

    lat = results["latency"]
    pc = results["prefix_cache"]
    ep = results["erepress"]
    print("\n## Results\n")
    print(f"- **E-3 TTFT (client proxy, n={lat['n']}):** "
          f"p50 {lat['ttft_ms_p50']:.0f} ms · p95 {lat['ttft_ms_p95']:.0f} ms · p99 {lat['ttft_ms_p99']:.0f} ms")
    print(f"- **E-4 decode:** median {lat['decode_chunks_per_s_median']:.1f} chunks/s "
          f"(median wall {lat['wall_s_median']:.2f} s)")
    print(f"- **E-2 prefix cache:** cold_cached={pc['cold_cached']} warm_max_cached={pc['warm_max_cached']} "
          f"active={pc['cache_active']}")
    print(f"- **E-5 erepress header:** X-Erepress={ep.get('x_erepress')} "
          f"worker={ep.get('worker_id')} routed={ep.get('routed_endpoint')}")


if __name__ == "__main__":
    main()
