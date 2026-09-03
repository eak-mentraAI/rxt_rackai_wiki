---
id: wf-{name}
type: workflow
status: draft
owner: team-or-role
domain: platform
aliases: []
related: []
source_docs: []
confidence: assumed
last_reviewed: YYYY-MM-DD
parent: hub-operations
summary: "One-line description of this workflow or state machine."
---

# {Workflow Name}

## Purpose

What this workflow accomplishes and when it runs.

## Trigger

What initiates this workflow (event, schedule, threshold, operator action).

## State Machine

```mermaid
stateDiagram-v2
    [*] --> State1
    State1 --> State2: condition
    State2 --> [*]
```

## Steps

1. Step — owner, formula/metric referenced, decision
2. …

## Events Emitted

| Event | When | Consumers |
|-------|------|-----------|
| [[evt-...]] | | |

## Dependencies

| Depends On | Type | Notes |
|------------|------|-------|
| [[...]] | DEPENDS_ON | |

## Ownership

Which team owns this workflow end to end.

## See Also

- [[Operations Hub]]
