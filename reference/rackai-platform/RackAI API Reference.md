---
title: "RackAI API Reference"
source: "https://docs.rackai.rax.io/user/api-reference/1.0.0/#tag/ModelDeployment/operation/patchNamespacedModelDeployment"
author:
published:
created: 2026-09-04
description:
tags:
  - "clippings"
---
## RackAI API (v1alpha1)

Download OpenAPI specification:[Download](https://docs.rackai.rax.io/user/api-reference/specs/1.0.0.yaml)

REST API for RackAI Custom Resources managed by the `rackai.rackspace.com` operator.

Most requests are routed through the Kubernetes API server and authenticated with a bearer token (service-account token or kubeconfig credential).

Organization management is the exception: tenants have no RBAC to edit the `Organization` custom resource directly, so those operations are served by the organizer service behind the Front Proxy and authenticated with an Auth0 OIDC token. See the **Organization** tag.

**Base path:** `/apis/rackai.rackspace.com/v1alpha1`

## ModelDeployment

ModelDeployment is a namespaced resource representing a deployed AI model instance. It references a `ModelClass` (which owns the Model identity and the runtime template); credentials are scoped via `spec.licenseCredential` (NGC) and `spec.imagePullCredentials` (image pull). Model-pull credentials live on the referenced Model's `spec.source.modelPullCredential`. The controller creates and manages an InferenceService on the GPU cluster for each ModelDeployment, and exposes the resulting inference endpoint via `status.inferenceEndpointURI`.

## List ModelDeployments in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeploymentList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "ModelDeployment", 		- "metadata": { 			- "name": "phoenix", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "acceleratorClass": "a100-40gb", 			- "args": [ 				- { 					- "name": "max-model-len", 					- "value": "16000" 					}, 				- { 					- "name": "enable-auto-tool-choice" 					}, 				- { 					- "name": "enable-lora", 					- "unset": true 					} 				], 			- "description": "Production chatbot endpoint backing the public docs assistant.", 			- "displayName": "Production Chatbot", 			- "env": [ 				- { 					- "name": "VLLM_LOGGING_LEVEL", 					- "value": "INFO" 					}, 				- { 					- "name": "NCCL_DEBUG", 					- "value": "WARN" 					}, 				- { 					- "name": "TRANSFORMERS_OFFLINE", 					- "unset": true 					} 				], 			- "imagePullCredentials": [ 				- "nvcr-pull-secret", 				- "platform-pull-secret" 				], 			- "licenseCredential": "ngc-license", 			- "loraAdapters": [ 				- "string" 				], 			- "modelClass": "qwen3-4b", 			- "resources": { 				- "limits": { 					- "cpu": "16", 					- "memory": "32Gi", 					- "nvidia.com/gpu": "2" 					}, 				- "requests": { 					- "cpu": "8", 					- "memory": "16Gi", 					- "nvidia.com/gpu": "2" 					} 				}, 			- "scaling": { 				- "maxReplicas": 1, 				- "minReplicas": 1 				}, 			- "sharedMemorySize": "16Gi" 			}, 		- "status": { 			- "accelerator": { 				- "name": [ 					- "string" 					], 				- "vendor": "string" 				}, 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "inferenceEndpointURI": "https://api.rackspace.com/apis/rackai.rackspace.com/v1alpha1/namespaces/my-org/inference/my-model", 			- "inferenceServiceRef": { 				- "apiGroup": "serving.kserve.io", 				- "kind": "InferenceService", 				- "name": "my-model-predictor", 				- "namespace": "my-org" 				}, 			- "internalInferenceURI": "http://my-model-predictor.my-org.svc.cluster.local/v2/models/my-model/infer", 			- "loadedLoRAAdapters": [ 				- "string" 				], 			- "loraReplicaStates": [ 				- { 					- "lastError": "string", 					- "lastSyncTime": "2019-08-24T14:15:22Z", 					- "loaded": [ 						- "string" 						], 					- "podName": "string" 					} 				], 			- "observedGeneration": 0, 			- "ready": false, 			- "replicas": { 				- "desired": 0, 				- "ready": 0 				}, 			- "runtimeImage": "amdenterpriseai/aim-base:0.11.1" 			} 		} 	] }`

## Create a ModelDeployment in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of ModelDeployment |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeployment", - "metadata": { 	- "name": "phoenix", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "a100-40gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "16000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			}, 		- { 			- "name": "enable-lora", 			- "unset": true 			} 		], 	- "description": "Production chatbot endpoint backing the public docs assistant.", 	- "displayName": "Production Chatbot", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "INFO" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "WARN" 			}, 		- { 			- "name": "TRANSFORMERS_OFFLINE", 			- "unset": true 			} 		], 	- "imagePullCredentials": [ 		- "nvcr-pull-secret", 		- "platform-pull-secret" 		], 	- "licenseCredential": "ngc-license", 	- "loraAdapters": [ 		- "string" 		], 	- "modelClass": "qwen3-4b", 	- "resources": { 		- "limits": { 			- "cpu": "16", 			- "memory": "32Gi", 			- "nvidia.com/gpu": "2" 			}, 		- "requests": { 			- "cpu": "8", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "2" 			} 		}, 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "16Gi" 	} }`

### Response samples

- 201
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeployment", - "metadata": { 	- "name": "phoenix", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "a100-40gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "16000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			}, 		- { 			- "name": "enable-lora", 			- "unset": true 			} 		], 	- "description": "Production chatbot endpoint backing the public docs assistant.", 	- "displayName": "Production Chatbot", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "INFO" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "WARN" 			}, 		- { 			- "name": "TRANSFORMERS_OFFLINE", 			- "unset": true 			} 		], 	- "imagePullCredentials": [ 		- "nvcr-pull-secret", 		- "platform-pull-secret" 		], 	- "licenseCredential": "ngc-license", 	- "loraAdapters": [ 		- "string" 		], 	- "modelClass": "qwen3-4b", 	- "resources": { 		- "limits": { 			- "cpu": "16", 			- "memory": "32Gi", 			- "nvidia.com/gpu": "2" 			}, 		- "requests": { 			- "cpu": "8", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "2" 			} 		}, 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "16Gi" 	}, - "status": { 	- "accelerator": { 		- "name": [ 			- "string" 			], 		- "vendor": "string" 		}, 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "inferenceEndpointURI": "https://api.rackspace.com/apis/rackai.rackspace.com/v1alpha1/namespaces/my-org/inference/my-model", 	- "inferenceServiceRef": { 		- "apiGroup": "serving.kserve.io", 		- "kind": "InferenceService", 		- "name": "my-model-predictor", 		- "namespace": "my-org" 		}, 	- "internalInferenceURI": "http://my-model-predictor.my-org.svc.cluster.local/v2/models/my-model/infer", 	- "loadedLoRAAdapters": [ 		- "string" 		], 	- "loraReplicaStates": [ 		- { 			- "lastError": "string", 			- "lastSyncTime": "2019-08-24T14:15:22Z", 			- "loaded": [ 				- "string" 				], 			- "podName": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": false, 	- "replicas": { 		- "desired": 0, 		- "ready": 0 		}, 	- "runtimeImage": "amdenterpriseai/aim-base:0.11.1" 	} }`

## Read a ModelDeployment

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeployment", - "metadata": { 	- "name": "phoenix", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "a100-40gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "16000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			}, 		- { 			- "name": "enable-lora", 			- "unset": true 			} 		], 	- "description": "Production chatbot endpoint backing the public docs assistant.", 	- "displayName": "Production Chatbot", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "INFO" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "WARN" 			}, 		- { 			- "name": "TRANSFORMERS_OFFLINE", 			- "unset": true 			} 		], 	- "imagePullCredentials": [ 		- "nvcr-pull-secret", 		- "platform-pull-secret" 		], 	- "licenseCredential": "ngc-license", 	- "loraAdapters": [ 		- "string" 		], 	- "modelClass": "qwen3-4b", 	- "resources": { 		- "limits": { 			- "cpu": "16", 			- "memory": "32Gi", 			- "nvidia.com/gpu": "2" 			}, 		- "requests": { 			- "cpu": "8", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "2" 			} 		}, 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "16Gi" 	}, - "status": { 	- "accelerator": { 		- "name": [ 			- "string" 			], 		- "vendor": "string" 		}, 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "inferenceEndpointURI": "https://api.rackspace.com/apis/rackai.rackspace.com/v1alpha1/namespaces/my-org/inference/my-model", 	- "inferenceServiceRef": { 		- "apiGroup": "serving.kserve.io", 		- "kind": "InferenceService", 		- "name": "my-model-predictor", 		- "namespace": "my-org" 		}, 	- "internalInferenceURI": "http://my-model-predictor.my-org.svc.cluster.local/v2/models/my-model/infer", 	- "loadedLoRAAdapters": [ 		- "string" 		], 	- "loraReplicaStates": [ 		- { 			- "lastError": "string", 			- "lastSyncTime": "2019-08-24T14:15:22Z", 			- "loaded": [ 				- "string" 				], 			- "podName": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": false, 	- "replicas": { 		- "desired": 0, 		- "ready": 0 		}, 	- "runtimeImage": "amdenterpriseai/aim-base:0.11.1" 	} }`

## Replace a ModelDeployment

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of ModelDeployment |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeployment", - "metadata": { 	- "name": "phoenix", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "a100-40gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "16000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			}, 		- { 			- "name": "enable-lora", 			- "unset": true 			} 		], 	- "description": "Production chatbot endpoint backing the public docs assistant.", 	- "displayName": "Production Chatbot", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "INFO" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "WARN" 			}, 		- { 			- "name": "TRANSFORMERS_OFFLINE", 			- "unset": true 			} 		], 	- "imagePullCredentials": [ 		- "nvcr-pull-secret", 		- "platform-pull-secret" 		], 	- "licenseCredential": "ngc-license", 	- "loraAdapters": [ 		- "string" 		], 	- "modelClass": "qwen3-4b", 	- "resources": { 		- "limits": { 			- "cpu": "16", 			- "memory": "32Gi", 			- "nvidia.com/gpu": "2" 			}, 		- "requests": { 			- "cpu": "8", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "2" 			} 		}, 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "16Gi" 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeployment", - "metadata": { 	- "name": "phoenix", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "a100-40gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "16000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			}, 		- { 			- "name": "enable-lora", 			- "unset": true 			} 		], 	- "description": "Production chatbot endpoint backing the public docs assistant.", 	- "displayName": "Production Chatbot", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "INFO" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "WARN" 			}, 		- { 			- "name": "TRANSFORMERS_OFFLINE", 			- "unset": true 			} 		], 	- "imagePullCredentials": [ 		- "nvcr-pull-secret", 		- "platform-pull-secret" 		], 	- "licenseCredential": "ngc-license", 	- "loraAdapters": [ 		- "string" 		], 	- "modelClass": "qwen3-4b", 	- "resources": { 		- "limits": { 			- "cpu": "16", 			- "memory": "32Gi", 			- "nvidia.com/gpu": "2" 			}, 		- "requests": { 			- "cpu": "8", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "2" 			} 		}, 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "16Gi" 	}, - "status": { 	- "accelerator": { 		- "name": [ 			- "string" 			], 		- "vendor": "string" 		}, 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "inferenceEndpointURI": "https://api.rackspace.com/apis/rackai.rackspace.com/v1alpha1/namespaces/my-org/inference/my-model", 	- "inferenceServiceRef": { 		- "apiGroup": "serving.kserve.io", 		- "kind": "InferenceService", 		- "name": "my-model-predictor", 		- "namespace": "my-org" 		}, 	- "internalInferenceURI": "http://my-model-predictor.my-org.svc.cluster.local/v2/models/my-model/infer", 	- "loadedLoRAAdapters": [ 		- "string" 		], 	- "loraReplicaStates": [ 		- { 			- "lastError": "string", 			- "lastSyncTime": "2019-08-24T14:15:22Z", 			- "loaded": [ 				- "string" 				], 			- "podName": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": false, 	- "replicas": { 		- "desired": 0, 		- "ready": 0 		}, 	- "runtimeImage": "amdenterpriseai/aim-base:0.11.1" 	} }`

## Partially update a ModelDeployment

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/merge-patch+jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of ModelDeployment |

### Responses

### Request samples

- Payload
Content type

application/merge-patch+json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeployment", - "metadata": { 	- "name": "phoenix", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "a100-40gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "16000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			}, 		- { 			- "name": "enable-lora", 			- "unset": true 			} 		], 	- "description": "Production chatbot endpoint backing the public docs assistant.", 	- "displayName": "Production Chatbot", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "INFO" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "WARN" 			}, 		- { 			- "name": "TRANSFORMERS_OFFLINE", 			- "unset": true 			} 		], 	- "imagePullCredentials": [ 		- "nvcr-pull-secret", 		- "platform-pull-secret" 		], 	- "licenseCredential": "ngc-license", 	- "loraAdapters": [ 		- "string" 		], 	- "modelClass": "qwen3-4b", 	- "resources": { 		- "limits": { 			- "cpu": "16", 			- "memory": "32Gi", 			- "nvidia.com/gpu": "2" 			}, 		- "requests": { 			- "cpu": "8", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "2" 			} 		}, 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "16Gi" 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeployment", - "metadata": { 	- "name": "phoenix", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "a100-40gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "16000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			}, 		- { 			- "name": "enable-lora", 			- "unset": true 			} 		], 	- "description": "Production chatbot endpoint backing the public docs assistant.", 	- "displayName": "Production Chatbot", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "INFO" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "WARN" 			}, 		- { 			- "name": "TRANSFORMERS_OFFLINE", 			- "unset": true 			} 		], 	- "imagePullCredentials": [ 		- "nvcr-pull-secret", 		- "platform-pull-secret" 		], 	- "licenseCredential": "ngc-license", 	- "loraAdapters": [ 		- "string" 		], 	- "modelClass": "qwen3-4b", 	- "resources": { 		- "limits": { 			- "cpu": "16", 			- "memory": "32Gi", 			- "nvidia.com/gpu": "2" 			}, 		- "requests": { 			- "cpu": "8", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "2" 			} 		}, 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "16Gi" 	}, - "status": { 	- "accelerator": { 		- "name": [ 			- "string" 			], 		- "vendor": "string" 		}, 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "inferenceEndpointURI": "https://api.rackspace.com/apis/rackai.rackspace.com/v1alpha1/namespaces/my-org/inference/my-model", 	- "inferenceServiceRef": { 		- "apiGroup": "serving.kserve.io", 		- "kind": "InferenceService", 		- "name": "my-model-predictor", 		- "namespace": "my-org" 		}, 	- "internalInferenceURI": "http://my-model-predictor.my-org.svc.cluster.local/v2/models/my-model/infer", 	- "loadedLoRAAdapters": [ 		- "string" 		], 	- "loraReplicaStates": [ 		- { 			- "lastError": "string", 			- "lastSyncTime": "2019-08-24T14:15:22Z", 			- "loaded": [ 				- "string" 				], 			- "podName": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": false, 	- "replicas": { 		- "desired": 0, 		- "ready": 0 		}, 	- "runtimeImage": "amdenterpriseai/aim-base:0.11.1" 	} }`

## Delete a ModelDeployment

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

## Read the status of a ModelDeployment

Returns the current `status` subresource of the ModelDeployment. The status is managed exclusively by the controller and cannot be updated by clients.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeployment", - "metadata": { 	- "name": "phoenix", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "a100-40gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "16000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			}, 		- { 			- "name": "enable-lora", 			- "unset": true 			} 		], 	- "description": "Production chatbot endpoint backing the public docs assistant.", 	- "displayName": "Production Chatbot", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "INFO" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "WARN" 			}, 		- { 			- "name": "TRANSFORMERS_OFFLINE", 			- "unset": true 			} 		], 	- "imagePullCredentials": [ 		- "nvcr-pull-secret", 		- "platform-pull-secret" 		], 	- "licenseCredential": "ngc-license", 	- "loraAdapters": [ 		- "string" 		], 	- "modelClass": "qwen3-4b", 	- "resources": { 		- "limits": { 			- "cpu": "16", 			- "memory": "32Gi", 			- "nvidia.com/gpu": "2" 			}, 		- "requests": { 			- "cpu": "8", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "2" 			} 		}, 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "16Gi" 	}, - "status": { 	- "accelerator": { 		- "name": [ 			- "string" 			], 		- "vendor": "string" 		}, 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "inferenceEndpointURI": "https://api.rackspace.com/apis/rackai.rackspace.com/v1alpha1/namespaces/my-org/inference/my-model", 	- "inferenceServiceRef": { 		- "apiGroup": "serving.kserve.io", 		- "kind": "InferenceService", 		- "name": "my-model-predictor", 		- "namespace": "my-org" 		}, 	- "internalInferenceURI": "http://my-model-predictor.my-org.svc.cluster.local/v2/models/my-model/infer", 	- "loadedLoRAAdapters": [ 		- "string" 		], 	- "loraReplicaStates": [ 		- { 			- "lastError": "string", 			- "lastSyncTime": "2019-08-24T14:15:22Z", 			- "loaded": [ 				- "string" 				], 			- "podName": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": false, 	- "replicas": { 		- "desired": 0, 		- "ready": 0 		}, 	- "runtimeImage": "amdenterpriseai/aim-base:0.11.1" 	} }`

## List ModelDeployments across all namespaces

##### Authorizations:

*BearerToken*

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelDeploymentList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "ModelDeployment", 		- "metadata": { 			- "name": "phoenix", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "acceleratorClass": "a100-40gb", 			- "args": [ 				- { 					- "name": "max-model-len", 					- "value": "16000" 					}, 				- { 					- "name": "enable-auto-tool-choice" 					}, 				- { 					- "name": "enable-lora", 					- "unset": true 					} 				], 			- "description": "Production chatbot endpoint backing the public docs assistant.", 			- "displayName": "Production Chatbot", 			- "env": [ 				- { 					- "name": "VLLM_LOGGING_LEVEL", 					- "value": "INFO" 					}, 				- { 					- "name": "NCCL_DEBUG", 					- "value": "WARN" 					}, 				- { 					- "name": "TRANSFORMERS_OFFLINE", 					- "unset": true 					} 				], 			- "imagePullCredentials": [ 				- "nvcr-pull-secret", 				- "platform-pull-secret" 				], 			- "licenseCredential": "ngc-license", 			- "loraAdapters": [ 				- "string" 				], 			- "modelClass": "qwen3-4b", 			- "resources": { 				- "limits": { 					- "cpu": "16", 					- "memory": "32Gi", 					- "nvidia.com/gpu": "2" 					}, 				- "requests": { 					- "cpu": "8", 					- "memory": "16Gi", 					- "nvidia.com/gpu": "2" 					} 				}, 			- "scaling": { 				- "maxReplicas": 1, 				- "minReplicas": 1 				}, 			- "sharedMemorySize": "16Gi" 			}, 		- "status": { 			- "accelerator": { 				- "name": [ 					- "string" 					], 				- "vendor": "string" 				}, 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "inferenceEndpointURI": "https://api.rackspace.com/apis/rackai.rackspace.com/v1alpha1/namespaces/my-org/inference/my-model", 			- "inferenceServiceRef": { 				- "apiGroup": "serving.kserve.io", 				- "kind": "InferenceService", 				- "name": "my-model-predictor", 				- "namespace": "my-org" 				}, 			- "internalInferenceURI": "http://my-model-predictor.my-org.svc.cluster.local/v2/models/my-model/infer", 			- "loadedLoRAAdapters": [ 				- "string" 				], 			- "loraReplicaStates": [ 				- { 					- "lastError": "string", 					- "lastSyncTime": "2019-08-24T14:15:22Z", 					- "loaded": [ 						- "string" 						], 					- "podName": "string" 					} 				], 			- "observedGeneration": 0, 			- "ready": false, 			- "replicas": { 				- "desired": 0, 				- "ready": 0 				}, 			- "runtimeImage": "amdenterpriseai/aim-base:0.11.1" 			} 		} 	] }`

## ModelClass

ModelClass is a namespaced deployment template for an AI model. It identifies the Model (via `spec.model`), the runtime (vllm/nim/...), and the runtime-level resources, scaling, image, and arguments. Many ModelDeployments may reference the same ModelClass; bootstrap may seed a set of ModelClass objects into each namespace.

## List ModelClasses in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClassList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "ModelClass", 		- "metadata": { 			- "name": "qwen3-4b", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "acceleratorClass": "h100-80gb", 			- "args": [ 				- { 					- "name": "max-model-len", 					- "value": "32000" 					}, 				- { 					- "name": "enable-auto-tool-choice" 					} 				], 			- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 			- "displayName": "Qwen3 4B (vLLM)", 			- "env": [ 				- { 					- "name": "VLLM_LOGGING_LEVEL", 					- "value": "DEBUG" 					}, 				- { 					- "name": "NCCL_DEBUG", 					- "value": "INFO" 					} 				], 			- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 			- "model": "llama3-8b-base", 			- "modelFormat": "vllmopenai", 			- "resources": { 				- "limits": { 					- "cpu": "12", 					- "memory": "16Gi", 					- "nvidia.com/gpu": "1" 					}, 				- "requests": { 					- "cpu": "6", 					- "memory": "8Gi", 					- "nvidia.com/gpu": "1" 					} 				}, 			- "runtime": "vllm", 			- "scaling": { 				- "maxReplicas": 1, 				- "minReplicas": 1 				}, 			- "sharedMemorySize": "8Gi" 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "observedGeneration": 0, 			- "ready": true 			} 		} 	] }`

## Create a ModelClass in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of ModelClass. |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClass", - "metadata": { 	- "name": "qwen3-4b", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "32000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			} 		], 	- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 	- "displayName": "Qwen3 4B (vLLM)", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "DEBUG" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "INFO" 			} 		], 	- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 	- "model": "llama3-8b-base", 	- "modelFormat": "vllmopenai", 	- "resources": { 		- "limits": { 			- "cpu": "12", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "1" 			}, 		- "requests": { 			- "cpu": "6", 			- "memory": "8Gi", 			- "nvidia.com/gpu": "1" 			} 		}, 	- "runtime": "vllm", 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "8Gi" 	} }`

### Response samples

- 201
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClass", - "metadata": { 	- "name": "qwen3-4b", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "32000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			} 		], 	- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 	- "displayName": "Qwen3 4B (vLLM)", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "DEBUG" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "INFO" 			} 		], 	- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 	- "model": "llama3-8b-base", 	- "modelFormat": "vllmopenai", 	- "resources": { 		- "limits": { 			- "cpu": "12", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "1" 			}, 		- "requests": { 			- "cpu": "6", 			- "memory": "8Gi", 			- "nvidia.com/gpu": "1" 			} 		}, 	- "runtime": "vllm", 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "8Gi" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": true 	} }`

## Read a ModelClass

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClass", - "metadata": { 	- "name": "qwen3-4b", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "32000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			} 		], 	- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 	- "displayName": "Qwen3 4B (vLLM)", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "DEBUG" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "INFO" 			} 		], 	- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 	- "model": "llama3-8b-base", 	- "modelFormat": "vllmopenai", 	- "resources": { 		- "limits": { 			- "cpu": "12", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "1" 			}, 		- "requests": { 			- "cpu": "6", 			- "memory": "8Gi", 			- "nvidia.com/gpu": "1" 			} 		}, 	- "runtime": "vllm", 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "8Gi" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": true 	} }`

## Replace a ModelClass

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of ModelClass. |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClass", - "metadata": { 	- "name": "qwen3-4b", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "32000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			} 		], 	- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 	- "displayName": "Qwen3 4B (vLLM)", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "DEBUG" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "INFO" 			} 		], 	- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 	- "model": "llama3-8b-base", 	- "modelFormat": "vllmopenai", 	- "resources": { 		- "limits": { 			- "cpu": "12", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "1" 			}, 		- "requests": { 			- "cpu": "6", 			- "memory": "8Gi", 			- "nvidia.com/gpu": "1" 			} 		}, 	- "runtime": "vllm", 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "8Gi" 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClass", - "metadata": { 	- "name": "qwen3-4b", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "32000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			} 		], 	- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 	- "displayName": "Qwen3 4B (vLLM)", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "DEBUG" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "INFO" 			} 		], 	- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 	- "model": "llama3-8b-base", 	- "modelFormat": "vllmopenai", 	- "resources": { 		- "limits": { 			- "cpu": "12", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "1" 			}, 		- "requests": { 			- "cpu": "6", 			- "memory": "8Gi", 			- "nvidia.com/gpu": "1" 			} 		}, 	- "runtime": "vllm", 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "8Gi" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": true 	} }`

## Partially update a ModelClass

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/merge-patch+jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of ModelClass. |

### Responses

### Request samples

- Payload
Content type

application/merge-patch+json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClass", - "metadata": { 	- "name": "qwen3-4b", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "32000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			} 		], 	- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 	- "displayName": "Qwen3 4B (vLLM)", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "DEBUG" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "INFO" 			} 		], 	- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 	- "model": "llama3-8b-base", 	- "modelFormat": "vllmopenai", 	- "resources": { 		- "limits": { 			- "cpu": "12", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "1" 			}, 		- "requests": { 			- "cpu": "6", 			- "memory": "8Gi", 			- "nvidia.com/gpu": "1" 			} 		}, 	- "runtime": "vllm", 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "8Gi" 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClass", - "metadata": { 	- "name": "qwen3-4b", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "32000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			} 		], 	- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 	- "displayName": "Qwen3 4B (vLLM)", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "DEBUG" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "INFO" 			} 		], 	- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 	- "model": "llama3-8b-base", 	- "modelFormat": "vllmopenai", 	- "resources": { 		- "limits": { 			- "cpu": "12", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "1" 			}, 		- "requests": { 			- "cpu": "6", 			- "memory": "8Gi", 			- "nvidia.com/gpu": "1" 			} 		}, 	- "runtime": "vllm", 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "8Gi" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": true 	} }`

## Delete a ModelClass

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

## Read the status of a ModelClass

Returns the current `status` subresource of the ModelClass. The status is managed exclusively by the controller and cannot be updated by clients.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClass", - "metadata": { 	- "name": "qwen3-4b", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "args": [ 		- { 			- "name": "max-model-len", 			- "value": "32000" 			}, 		- { 			- "name": "enable-auto-tool-choice" 			} 		], 	- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 	- "displayName": "Qwen3 4B (vLLM)", 	- "env": [ 		- { 			- "name": "VLLM_LOGGING_LEVEL", 			- "value": "DEBUG" 			}, 		- { 			- "name": "NCCL_DEBUG", 			- "value": "INFO" 			} 		], 	- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 	- "model": "llama3-8b-base", 	- "modelFormat": "vllmopenai", 	- "resources": { 		- "limits": { 			- "cpu": "12", 			- "memory": "16Gi", 			- "nvidia.com/gpu": "1" 			}, 		- "requests": { 			- "cpu": "6", 			- "memory": "8Gi", 			- "nvidia.com/gpu": "1" 			} 		}, 	- "runtime": "vllm", 	- "scaling": { 		- "maxReplicas": 1, 		- "minReplicas": 1 		}, 	- "sharedMemorySize": "8Gi" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "observedGeneration": 0, 	- "ready": true 	} }`

## List ModelClasses across all namespaces

##### Authorizations:

*BearerToken*

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelClassList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "ModelClass", 		- "metadata": { 			- "name": "qwen3-4b", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "acceleratorClass": "h100-80gb", 			- "args": [ 				- { 					- "name": "max-model-len", 					- "value": "32000" 					}, 				- { 					- "name": "enable-auto-tool-choice" 					} 				], 			- "description": "vLLM-optimized template for low-latency chat serving with tool use.", 			- "displayName": "Qwen3 4B (vLLM)", 			- "env": [ 				- { 					- "name": "VLLM_LOGGING_LEVEL", 					- "value": "DEBUG" 					}, 				- { 					- "name": "NCCL_DEBUG", 					- "value": "INFO" 					} 				], 			- "image": "nvcr.io/nim/deepseek-ai/deepseek-r1:1.0.0", 			- "model": "llama3-8b-base", 			- "modelFormat": "vllmopenai", 			- "resources": { 				- "limits": { 					- "cpu": "12", 					- "memory": "16Gi", 					- "nvidia.com/gpu": "1" 					}, 				- "requests": { 					- "cpu": "6", 					- "memory": "8Gi", 					- "nvidia.com/gpu": "1" 					} 				}, 			- "runtime": "vllm", 			- "scaling": { 				- "maxReplicas": 1, 				- "minReplicas": 1 				}, 			- "sharedMemorySize": "8Gi" 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "observedGeneration": 0, 			- "ready": true 			} 		} 	] }`

## RegistryCredential

RegistryCredential is a namespaced resource carrying one Secret of one purpose (modelPull, license, imagePull). Each RegistryCredential carries exactly one Secret with exactly one purpose (Type); namespaces typically hold several. Referenced by Model's `spec.source.modelPullCredential` for weight fetching, and by ModelDeployment's `spec.licenseCredential` / `spec.imagePullCredentials` for runtime container needs.

## List RegistryCredentials in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredentialList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "RegistryCredential", 		- "metadata": { 			- "name": "huggingface-token", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "description": "HuggingFace organization token for the acme-corp team", 			- "displayName": "HuggingFace Org Token", 			- "secret": "hf-modelpull-token", 			- "type": "modelPull" 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "usedBy": [ 				- "string" 				] 			} 		} 	] }`

## Create a RegistryCredential in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of RegistryCredential. |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredential", - "metadata": { 	- "name": "huggingface-token", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "HuggingFace organization token for the acme-corp team", 	- "displayName": "HuggingFace Org Token", 	- "secret": "hf-modelpull-token", 	- "type": "modelPull" 	} }`

### Response samples

- 201
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredential", - "metadata": { 	- "name": "huggingface-token", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "HuggingFace organization token for the acme-corp team", 	- "displayName": "HuggingFace Org Token", 	- "secret": "hf-modelpull-token", 	- "type": "modelPull" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "usedBy": [ 		- "string" 		] 	} }`

## Read a RegistryCredential

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredential", - "metadata": { 	- "name": "huggingface-token", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "HuggingFace organization token for the acme-corp team", 	- "displayName": "HuggingFace Org Token", 	- "secret": "hf-modelpull-token", 	- "type": "modelPull" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "usedBy": [ 		- "string" 		] 	} }`

## Replace a RegistryCredential

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of RegistryCredential. |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredential", - "metadata": { 	- "name": "huggingface-token", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "HuggingFace organization token for the acme-corp team", 	- "displayName": "HuggingFace Org Token", 	- "secret": "hf-modelpull-token", 	- "type": "modelPull" 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredential", - "metadata": { 	- "name": "huggingface-token", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "HuggingFace organization token for the acme-corp team", 	- "displayName": "HuggingFace Org Token", 	- "secret": "hf-modelpull-token", 	- "type": "modelPull" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "usedBy": [ 		- "string" 		] 	} }`

## Partially update a RegistryCredential

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/merge-patch+jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of RegistryCredential. |

### Responses

### Request samples

- Payload
Content type

application/merge-patch+json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredential", - "metadata": { 	- "name": "huggingface-token", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "HuggingFace organization token for the acme-corp team", 	- "displayName": "HuggingFace Org Token", 	- "secret": "hf-modelpull-token", 	- "type": "modelPull" 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredential", - "metadata": { 	- "name": "huggingface-token", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "HuggingFace organization token for the acme-corp team", 	- "displayName": "HuggingFace Org Token", 	- "secret": "hf-modelpull-token", 	- "type": "modelPull" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "usedBy": [ 		- "string" 		] 	} }`

## Delete a RegistryCredential

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

## Read the status of a RegistryCredential

Returns the current `status` subresource of the RegistryCredential. The status is managed exclusively by the controller and cannot be updated by clients.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredential", - "metadata": { 	- "name": "huggingface-token", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "HuggingFace organization token for the acme-corp team", 	- "displayName": "HuggingFace Org Token", 	- "secret": "hf-modelpull-token", 	- "type": "modelPull" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "usedBy": [ 		- "string" 		] 	} }`

## List RegistryCredentials across all namespaces

##### Authorizations:

*BearerToken*

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "RegistryCredentialList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "RegistryCredential", 		- "metadata": { 			- "name": "huggingface-token", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "description": "HuggingFace organization token for the acme-corp team", 			- "displayName": "HuggingFace Org Token", 			- "secret": "hf-modelpull-token", 			- "type": "modelPull" 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "usedBy": [ 				- "string" 				] 			} 		} 	] }`

## Organization

Organization represents a tenant in the RackAI platform. The controller provisions a dedicated Kubernetes namespace and RBAC policies for each Organization, isolating its workloads (Models, ModelClasses, ModelDeployments, RegistryCredentials, LoRAAdapters, Datasets, FineTuningJobs) from other tenants. The resulting namespace is reported in status.namespace.

## List the caller's organizations

Returns the Auth0 organizations the authenticated user is a member of. The organizer adds a `namespace` entry to each organization's `metadata` (the Auth0 organization ID normalized to its Kubernetes namespace).

##### Authorizations:

*Auth0Bearer*

### Responses

### Response samples

- 200
Content type

application/json

`{ - "organizations": [ 	- { 		- "id": "org_xxxxxxxxxxxxxxxx", 		- "name": "acme-corp", 		- "display_name": "Acme Corp", 		- "branding": { 			- "logo_url": "http://example.com" 			}, 		- "metadata": { 			- "namespace": "org-xxxxxxxxxxxxxxxx" 			} 		} 	], - "start": 0, - "limit": 50, - "length": 1, - "total": 1, - "next": "string" }`

## Create an organization

Creates an Auth0 organization, enables the available connections, adds the caller as a member, and creates the backing `Organization` custom resource (which provisions the tenant namespace and seeds the catalog). The `name` must be URL-safe and must not begin with `org-`.

##### Authorizations:

*Auth0Bearer*

##### Request Body schema: application/jsonrequired

| name  required | string  URL-safe organization name. Must not begin with `org-`. |
| --- | --- |
| display\_name | string |
| branding | object |
| metadata | object  Arbitrary string key/value metadata stored on the organization. |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "name": "acme-corp", - "display_name": "Acme Corp", - "branding": { 	- "logo_url": "https://cdn.example.com/acme/logo.png" 	}, - "metadata": { 	- "tier": "standard" 	} }`

### Response samples

- 200
Content type

application/json

`{ - "orgId": "org_xxxxxxxxxxxxxxxx" }`

## Delete an organization

Deletes the backing `Organization` custom resource and then the Auth0 organization. The caller must be a member of the organization. `org_id` is the Auth0 organization ID (prefixed with `org_`).

##### Authorizations:

*Auth0Bearer*

##### path Parameters

| org\_id  required | string  Example: org\_xxxxxxxxxxxxxxxx  Auth0 organization ID (prefixed with `org_`). |
| --- | --- |

### Responses

## Look up an organization by name

Public endpoint. Resolves an organization by its name and returns its Auth0 organization record. Used during login to discover which organization a user is signing in to.

##### path Parameters

| name  required | string  Name of the resource. |
| --- | --- |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "id": "org_xxxxxxxxxxxxxxxx", - "name": "acme-corp", - "display_name": "Acme Corp", - "branding": { 	- "logo_url": "http://example.com" 	}, - "metadata": { 	- "namespace": "org-xxxxxxxxxxxxxxxx" 	} }`

## Dataset

Dataset represents a training or validation dataset within a namespace. It supports "text" and "messages" formats and can optionally verify file integrity via MD5 checksums. The storage path is inferred from the object's namespace and name in SeaweedFS — no URI needs to be specified by the user. The controller confirms file presence, lists files, and runs integrity checks.

## List Datasets in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "DatasetList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "Dataset", 		- "metadata": { 			- "name": "alpaca-train", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "description": "Alpaca instruction-tuning dataset, training split.", 			- "displayName": "Alpaca Training Split", 			- "format": "messages", 			- "integrity": { 				- "md5": { 					- "property1": "string", 					- "property2": "string" 					} 				} 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "file": "string", 			- "files": [ 				- { 					- "path": "string", 					- "size": 0 					} 				], 			- "integrity": { 				- "files": { 					- "property1": { 						- "md5": "string", 						- "size": 0 						}, 					- "property2": { 						- "md5": "string", 						- "size": 0 						} 					} 				}, 			- "observedGeneration": 0, 			- "phase": "Pending", 			- "pvName": "string", 			- "pvcName": "string", 			- "ready": true, 			- "storageRef": { 				- "inferredPath": "string" 				} 			} 		} 	] }`

## Create a Dataset in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  spec defines the desired state of Dataset |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Dataset", - "metadata": { 	- "name": "alpaca-train", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "Alpaca instruction-tuning dataset, training split.", 	- "displayName": "Alpaca Training Split", 	- "format": "messages", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		} 	} }`

### Response samples

- 201
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Dataset", - "metadata": { 	- "name": "alpaca-train", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "Alpaca instruction-tuning dataset, training split.", 	- "displayName": "Alpaca Training Split", 	- "format": "messages", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		} 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "file": "string", 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "files": { 			- "property1": { 				- "md5": "string", 				- "size": 0 				}, 			- "property2": { 				- "md5": "string", 				- "size": 0 				} 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "pvName": "string", 	- "pvcName": "string", 	- "ready": true, 	- "storageRef": { 		- "inferredPath": "string" 		} 	} }`

## Read a Dataset

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Dataset", - "metadata": { 	- "name": "alpaca-train", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "Alpaca instruction-tuning dataset, training split.", 	- "displayName": "Alpaca Training Split", 	- "format": "messages", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		} 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "file": "string", 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "files": { 			- "property1": { 				- "md5": "string", 				- "size": 0 				}, 			- "property2": { 				- "md5": "string", 				- "size": 0 				} 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "pvName": "string", 	- "pvcName": "string", 	- "ready": true, 	- "storageRef": { 		- "inferredPath": "string" 		} 	} }`

## Delete a Dataset

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

## Read the status of a Dataset

Returns the current `status` subresource of the Dataset. The status is managed exclusively by the controller and cannot be updated by clients.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Dataset", - "metadata": { 	- "name": "alpaca-train", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "description": "Alpaca instruction-tuning dataset, training split.", 	- "displayName": "Alpaca Training Split", 	- "format": "messages", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		} 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "file": "string", 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "files": { 			- "property1": { 				- "md5": "string", 				- "size": 0 				}, 			- "property2": { 				- "md5": "string", 				- "size": 0 				} 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "pvName": "string", 	- "pvcName": "string", 	- "ready": true, 	- "storageRef": { 		- "inferredPath": "string" 		} 	} }`

## Upload a file to a Dataset

Uploads a single file to the Dataset's storage directory in SeaweedFS. The front proxy routes this request based on the `x-upload-target` header.

To upload an entire directory, call this endpoint once per file, preserving the relative path in the `{filePath}` parameter.

After all files are uploaded, the Dataset controller verifies file presence and (if configured) MD5 integrity, then sets `status.ready = true`.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |
| filePath  required | string  Remote file path within the artifact's storage directory. When uploading a directory tree, this preserves the relative path structure (e.g. `subdir/data.parquet`). May contain forward slashes for nested paths; the Envoy front proxy handles the full path via regex routing. |

##### header Parameters

| x-upload-target  required | string  Value: "datasets"  Must be set to `datasets` for dataset file uploads. |
| --- | --- |
| Content-MD5 | string  Example: d0e972641a9148f265e5ec218f1fc3cc  Hex-encoded MD5 digest of the file being uploaded. When provided, the server verifies the uploaded file's integrity against this value during upload. For Model and Dataset uploads, corresponds to the `spec.integrity.md5` field on the resource. |

##### Request Body schema: multipart/form-datarequired

Single-file upload as multipart/form-data. The `file` part carries the raw file content.

| file  required | string \<binary>  The file content to upload. |
| --- | --- |

### Responses

## List Datasets across all namespaces

##### Authorizations:

*BearerToken*

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "DatasetList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "Dataset", 		- "metadata": { 			- "name": "alpaca-train", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "description": "Alpaca instruction-tuning dataset, training split.", 			- "displayName": "Alpaca Training Split", 			- "format": "messages", 			- "integrity": { 				- "md5": { 					- "property1": "string", 					- "property2": "string" 					} 				} 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "file": "string", 			- "files": [ 				- { 					- "path": "string", 					- "size": 0 					} 				], 			- "integrity": { 				- "files": { 					- "property1": { 						- "md5": "string", 						- "size": 0 						}, 					- "property2": { 						- "md5": "string", 						- "size": 0 						} 					} 				}, 			- "observedGeneration": 0, 			- "phase": "Pending", 			- "pvName": "string", 			- "pvcName": "string", 			- "ready": true, 			- "storageRef": { 				- "inferredPath": "string" 				} 			} 		} 	] }`

## FineTuningJob

FineTuningJob orchestrates an LLM fine-tuning run within a namespace. It manages a multi-phase pipeline: training (with LoRA/QLoRA PEFT), optional post-training evaluation comparing adapter quality against the base model, and adapter upload to produce a LoRAAdapter resource. The controller creates Kubernetes Jobs for each phase and tracks progress via status conditions.

## List FineTuningJobs in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJobList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "FineTuningJob", 		- "metadata": { 			- "name": "llama3-lora-finetune", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "acceleratorClass": "h100-80gb", 			- "datasets": [ 				- { 					- "name": "alpaca-train", 					- "type": "training" 					} 				], 			- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 			- "displayName": "Sprint 3 SFT Run", 			- "peft": { 				- "loraAlpha": 1, 				- "loraDropout": "string", 				- "loraR": 1, 				- "targetModules": [ 					- "string" 					], 				- "useQlora": true 				}, 			- "resources": { 				- "claims": [ 					- { 						- "name": "string", 						- "request": "string" 						} 					], 				- "limits": { 					- "property1": 0, 					- "property2": 0 					}, 				- "requests": { 					- "property1": 0, 					- "property2": 0 					} 				}, 			- "training": { 				- "baseModel": "llama3-8b-base", 				- "batchSize": 0, 				- "bf16": true, 				- "earlyStopping": { 					- "enabled": false, 					- "greaterIsBetter": false, 					- "metric": "eval_loss", 					- "patience": 3, 					- "threshold": "0.0" 					}, 				- "evalSteps": 20, 				- "fp16": false, 				- "gradientAccumulationSteps": 0, 				- "jobType": "SFT", 				- "learningRate": "2e-4", 				- "learningRateWarmupSteps": 0, 				- "loggingSteps": 1, 				- "maxLength": 0, 				- "numEpochs": 0, 				- "saveIntervalSteps": -1, 				- "seed": 42, 				- "validationSplitPercentage": 10 				}, 			- "workPVC": { 				- "accessModes": [ 					- "string" 					], 				- "claimName": "string", 				- "mountPath": "string", 				- "selector": { 					- "property1": "string", 					- "property2": "string" 					}, 				- "size": "50Gi", 				- "storageClassName": "string", 				- "volumeName": "string" 				} 			}, 		- "status": { 			- "artifacts": { 				- "adaptersDir": "string", 				- "donePath": "string", 				- "earlyStopPath": "string", 				- "errorPath": "string", 				- "failedPath": "string", 				- "metricsPath": "string", 				- "outputDir": "string", 				- "runConfigPath": "string", 				- "startedPath": "string", 				- "summaryPath": "string", 				- "tensorBoardDir": "string", 				- "workDir": "string" 				}, 			- "completedAt": "2019-08-24T14:15:22Z", 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "duration": "string", 			- "evaluation": { 				- "evalPath": "string", 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "message": "string", 				- "metrics": { 					- "adapterEvalLoss": "string", 					- "adapterPPL": "string", 					- "baselineEvalLoss": "string", 					- "baselinePPL": "string", 					- "deltaEvalLoss": "string", 					- "deltaPPLPercent": "string" 					}, 				- "phase": "Pending", 				- "result": "Unknown" 				}, 			- "loraAdapterUpload": { 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "loraAdapterName": "string", 				- "message": "string", 				- "phase": "Pending", 				- "result": "Unknown" 				}, 			- "message": "string", 			- "observedGeneration": 0, 			- "phase": "Pending", 			- "preprocessing": { 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "message": "string", 				- "phase": "Pending", 				- "result": "Unknown" 				}, 			- "resolvedTrainingParams": { 				- "baseModel": "string", 				- "batchSize": 0, 				- "bf16": true, 				- "earlyStopping": { 					- "enabled": false, 					- "greaterIsBetter": false, 					- "metric": "eval_loss", 					- "patience": 3, 					- "threshold": "0.0" 					}, 				- "epochs": 0, 				- "evalInterval": 0, 				- "fp16": true, 				- "gradientAccumulation": 0, 				- "isCompatible": true, 				- "learningRate": "string", 				- "learningRateWarmupSteps": 0, 				- "loggingInterval": 0, 				- "loraAlpha": 0, 				- "loraDropout": "string", 				- "loraRank": 0, 				- "maxContextLength": 0, 				- "recipeId": "string", 				- "saveInterval": 0, 				- "seed": 0, 				- "targetModules": [ 					- "string" 					], 				- "useQlora": true, 				- "validationSplitPercentage": 0 				}, 			- "training": { 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "message": "string", 				- "phase": "Pending", 				- "result": "Unknown" 				}, 			- "validation": { 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "message": "string", 				- "phase": "Pending", 				- "result": "Unknown" 				} 			} 		} 	] }`

## Create a FineTuningJob in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  spec defines the desired state of FineTuningJob |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJob", - "metadata": { 	- "name": "llama3-lora-finetune", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "datasets": [ 		- { 			- "name": "alpaca-train", 			- "type": "training" 			} 		], 	- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 	- "displayName": "Sprint 3 SFT Run", 	- "peft": { 		- "loraAlpha": 1, 		- "loraDropout": "string", 		- "loraR": 1, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true 		}, 	- "resources": { 		- "claims": [ 			- { 				- "name": "string", 				- "request": "string" 				} 			], 		- "limits": { 			- "property1": 0, 			- "property2": 0 			}, 		- "requests": { 			- "property1": 0, 			- "property2": 0 			} 		}, 	- "training": { 		- "baseModel": "llama3-8b-base", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "evalSteps": 20, 		- "fp16": false, 		- "gradientAccumulationSteps": 0, 		- "jobType": "SFT", 		- "learningRate": "2e-4", 		- "learningRateWarmupSteps": 0, 		- "loggingSteps": 1, 		- "maxLength": 0, 		- "numEpochs": 0, 		- "saveIntervalSteps": -1, 		- "seed": 42, 		- "validationSplitPercentage": 10 		}, 	- "workPVC": { 		- "accessModes": [ 			- "string" 			], 		- "claimName": "string", 		- "mountPath": "string", 		- "selector": { 			- "property1": "string", 			- "property2": "string" 			}, 		- "size": "50Gi", 		- "storageClassName": "string", 		- "volumeName": "string" 		} 	} }`

### Response samples

- 201
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJob", - "metadata": { 	- "name": "llama3-lora-finetune", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "datasets": [ 		- { 			- "name": "alpaca-train", 			- "type": "training" 			} 		], 	- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 	- "displayName": "Sprint 3 SFT Run", 	- "peft": { 		- "loraAlpha": 1, 		- "loraDropout": "string", 		- "loraR": 1, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true 		}, 	- "resources": { 		- "claims": [ 			- { 				- "name": "string", 				- "request": "string" 				} 			], 		- "limits": { 			- "property1": 0, 			- "property2": 0 			}, 		- "requests": { 			- "property1": 0, 			- "property2": 0 			} 		}, 	- "training": { 		- "baseModel": "llama3-8b-base", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "evalSteps": 20, 		- "fp16": false, 		- "gradientAccumulationSteps": 0, 		- "jobType": "SFT", 		- "learningRate": "2e-4", 		- "learningRateWarmupSteps": 0, 		- "loggingSteps": 1, 		- "maxLength": 0, 		- "numEpochs": 0, 		- "saveIntervalSteps": -1, 		- "seed": 42, 		- "validationSplitPercentage": 10 		}, 	- "workPVC": { 		- "accessModes": [ 			- "string" 			], 		- "claimName": "string", 		- "mountPath": "string", 		- "selector": { 			- "property1": "string", 			- "property2": "string" 			}, 		- "size": "50Gi", 		- "storageClassName": "string", 		- "volumeName": "string" 		} 	}, - "status": { 	- "artifacts": { 		- "adaptersDir": "string", 		- "donePath": "string", 		- "earlyStopPath": "string", 		- "errorPath": "string", 		- "failedPath": "string", 		- "metricsPath": "string", 		- "outputDir": "string", 		- "runConfigPath": "string", 		- "startedPath": "string", 		- "summaryPath": "string", 		- "tensorBoardDir": "string", 		- "workDir": "string" 		}, 	- "completedAt": "2019-08-24T14:15:22Z", 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "duration": "string", 	- "evaluation": { 		- "evalPath": "string", 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "metrics": { 			- "adapterEvalLoss": "string", 			- "adapterPPL": "string", 			- "baselineEvalLoss": "string", 			- "baselinePPL": "string", 			- "deltaEvalLoss": "string", 			- "deltaPPLPercent": "string" 			}, 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "loraAdapterUpload": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "loraAdapterName": "string", 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "message": "string", 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "preprocessing": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "resolvedTrainingParams": { 		- "baseModel": "string", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "epochs": 0, 		- "evalInterval": 0, 		- "fp16": true, 		- "gradientAccumulation": 0, 		- "isCompatible": true, 		- "learningRate": "string", 		- "learningRateWarmupSteps": 0, 		- "loggingInterval": 0, 		- "loraAlpha": 0, 		- "loraDropout": "string", 		- "loraRank": 0, 		- "maxContextLength": 0, 		- "recipeId": "string", 		- "saveInterval": 0, 		- "seed": 0, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true, 		- "validationSplitPercentage": 0 		}, 	- "training": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "validation": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		} 	} }`

## Read a FineTuningJob

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJob", - "metadata": { 	- "name": "llama3-lora-finetune", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "datasets": [ 		- { 			- "name": "alpaca-train", 			- "type": "training" 			} 		], 	- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 	- "displayName": "Sprint 3 SFT Run", 	- "peft": { 		- "loraAlpha": 1, 		- "loraDropout": "string", 		- "loraR": 1, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true 		}, 	- "resources": { 		- "claims": [ 			- { 				- "name": "string", 				- "request": "string" 				} 			], 		- "limits": { 			- "property1": 0, 			- "property2": 0 			}, 		- "requests": { 			- "property1": 0, 			- "property2": 0 			} 		}, 	- "training": { 		- "baseModel": "llama3-8b-base", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "evalSteps": 20, 		- "fp16": false, 		- "gradientAccumulationSteps": 0, 		- "jobType": "SFT", 		- "learningRate": "2e-4", 		- "learningRateWarmupSteps": 0, 		- "loggingSteps": 1, 		- "maxLength": 0, 		- "numEpochs": 0, 		- "saveIntervalSteps": -1, 		- "seed": 42, 		- "validationSplitPercentage": 10 		}, 	- "workPVC": { 		- "accessModes": [ 			- "string" 			], 		- "claimName": "string", 		- "mountPath": "string", 		- "selector": { 			- "property1": "string", 			- "property2": "string" 			}, 		- "size": "50Gi", 		- "storageClassName": "string", 		- "volumeName": "string" 		} 	}, - "status": { 	- "artifacts": { 		- "adaptersDir": "string", 		- "donePath": "string", 		- "earlyStopPath": "string", 		- "errorPath": "string", 		- "failedPath": "string", 		- "metricsPath": "string", 		- "outputDir": "string", 		- "runConfigPath": "string", 		- "startedPath": "string", 		- "summaryPath": "string", 		- "tensorBoardDir": "string", 		- "workDir": "string" 		}, 	- "completedAt": "2019-08-24T14:15:22Z", 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "duration": "string", 	- "evaluation": { 		- "evalPath": "string", 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "metrics": { 			- "adapterEvalLoss": "string", 			- "adapterPPL": "string", 			- "baselineEvalLoss": "string", 			- "baselinePPL": "string", 			- "deltaEvalLoss": "string", 			- "deltaPPLPercent": "string" 			}, 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "loraAdapterUpload": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "loraAdapterName": "string", 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "message": "string", 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "preprocessing": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "resolvedTrainingParams": { 		- "baseModel": "string", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "epochs": 0, 		- "evalInterval": 0, 		- "fp16": true, 		- "gradientAccumulation": 0, 		- "isCompatible": true, 		- "learningRate": "string", 		- "learningRateWarmupSteps": 0, 		- "loggingInterval": 0, 		- "loraAlpha": 0, 		- "loraDropout": "string", 		- "loraRank": 0, 		- "maxContextLength": 0, 		- "recipeId": "string", 		- "saveInterval": 0, 		- "seed": 0, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true, 		- "validationSplitPercentage": 0 		}, 	- "training": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "validation": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		} 	} }`

## Replace a FineTuningJob

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  spec defines the desired state of FineTuningJob |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJob", - "metadata": { 	- "name": "llama3-lora-finetune", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "datasets": [ 		- { 			- "name": "alpaca-train", 			- "type": "training" 			} 		], 	- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 	- "displayName": "Sprint 3 SFT Run", 	- "peft": { 		- "loraAlpha": 1, 		- "loraDropout": "string", 		- "loraR": 1, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true 		}, 	- "resources": { 		- "claims": [ 			- { 				- "name": "string", 				- "request": "string" 				} 			], 		- "limits": { 			- "property1": 0, 			- "property2": 0 			}, 		- "requests": { 			- "property1": 0, 			- "property2": 0 			} 		}, 	- "training": { 		- "baseModel": "llama3-8b-base", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "evalSteps": 20, 		- "fp16": false, 		- "gradientAccumulationSteps": 0, 		- "jobType": "SFT", 		- "learningRate": "2e-4", 		- "learningRateWarmupSteps": 0, 		- "loggingSteps": 1, 		- "maxLength": 0, 		- "numEpochs": 0, 		- "saveIntervalSteps": -1, 		- "seed": 42, 		- "validationSplitPercentage": 10 		}, 	- "workPVC": { 		- "accessModes": [ 			- "string" 			], 		- "claimName": "string", 		- "mountPath": "string", 		- "selector": { 			- "property1": "string", 			- "property2": "string" 			}, 		- "size": "50Gi", 		- "storageClassName": "string", 		- "volumeName": "string" 		} 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJob", - "metadata": { 	- "name": "llama3-lora-finetune", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "datasets": [ 		- { 			- "name": "alpaca-train", 			- "type": "training" 			} 		], 	- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 	- "displayName": "Sprint 3 SFT Run", 	- "peft": { 		- "loraAlpha": 1, 		- "loraDropout": "string", 		- "loraR": 1, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true 		}, 	- "resources": { 		- "claims": [ 			- { 				- "name": "string", 				- "request": "string" 				} 			], 		- "limits": { 			- "property1": 0, 			- "property2": 0 			}, 		- "requests": { 			- "property1": 0, 			- "property2": 0 			} 		}, 	- "training": { 		- "baseModel": "llama3-8b-base", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "evalSteps": 20, 		- "fp16": false, 		- "gradientAccumulationSteps": 0, 		- "jobType": "SFT", 		- "learningRate": "2e-4", 		- "learningRateWarmupSteps": 0, 		- "loggingSteps": 1, 		- "maxLength": 0, 		- "numEpochs": 0, 		- "saveIntervalSteps": -1, 		- "seed": 42, 		- "validationSplitPercentage": 10 		}, 	- "workPVC": { 		- "accessModes": [ 			- "string" 			], 		- "claimName": "string", 		- "mountPath": "string", 		- "selector": { 			- "property1": "string", 			- "property2": "string" 			}, 		- "size": "50Gi", 		- "storageClassName": "string", 		- "volumeName": "string" 		} 	}, - "status": { 	- "artifacts": { 		- "adaptersDir": "string", 		- "donePath": "string", 		- "earlyStopPath": "string", 		- "errorPath": "string", 		- "failedPath": "string", 		- "metricsPath": "string", 		- "outputDir": "string", 		- "runConfigPath": "string", 		- "startedPath": "string", 		- "summaryPath": "string", 		- "tensorBoardDir": "string", 		- "workDir": "string" 		}, 	- "completedAt": "2019-08-24T14:15:22Z", 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "duration": "string", 	- "evaluation": { 		- "evalPath": "string", 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "metrics": { 			- "adapterEvalLoss": "string", 			- "adapterPPL": "string", 			- "baselineEvalLoss": "string", 			- "baselinePPL": "string", 			- "deltaEvalLoss": "string", 			- "deltaPPLPercent": "string" 			}, 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "loraAdapterUpload": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "loraAdapterName": "string", 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "message": "string", 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "preprocessing": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "resolvedTrainingParams": { 		- "baseModel": "string", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "epochs": 0, 		- "evalInterval": 0, 		- "fp16": true, 		- "gradientAccumulation": 0, 		- "isCompatible": true, 		- "learningRate": "string", 		- "learningRateWarmupSteps": 0, 		- "loggingInterval": 0, 		- "loraAlpha": 0, 		- "loraDropout": "string", 		- "loraRank": 0, 		- "maxContextLength": 0, 		- "recipeId": "string", 		- "saveInterval": 0, 		- "seed": 0, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true, 		- "validationSplitPercentage": 0 		}, 	- "training": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "validation": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		} 	} }`

## Partially update a FineTuningJob

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/merge-patch+jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  spec defines the desired state of FineTuningJob |

### Responses

### Request samples

- Payload
Content type

application/merge-patch+json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJob", - "metadata": { 	- "name": "llama3-lora-finetune", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "datasets": [ 		- { 			- "name": "alpaca-train", 			- "type": "training" 			} 		], 	- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 	- "displayName": "Sprint 3 SFT Run", 	- "peft": { 		- "loraAlpha": 1, 		- "loraDropout": "string", 		- "loraR": 1, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true 		}, 	- "resources": { 		- "claims": [ 			- { 				- "name": "string", 				- "request": "string" 				} 			], 		- "limits": { 			- "property1": 0, 			- "property2": 0 			}, 		- "requests": { 			- "property1": 0, 			- "property2": 0 			} 		}, 	- "training": { 		- "baseModel": "llama3-8b-base", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "evalSteps": 20, 		- "fp16": false, 		- "gradientAccumulationSteps": 0, 		- "jobType": "SFT", 		- "learningRate": "2e-4", 		- "learningRateWarmupSteps": 0, 		- "loggingSteps": 1, 		- "maxLength": 0, 		- "numEpochs": 0, 		- "saveIntervalSteps": -1, 		- "seed": 42, 		- "validationSplitPercentage": 10 		}, 	- "workPVC": { 		- "accessModes": [ 			- "string" 			], 		- "claimName": "string", 		- "mountPath": "string", 		- "selector": { 			- "property1": "string", 			- "property2": "string" 			}, 		- "size": "50Gi", 		- "storageClassName": "string", 		- "volumeName": "string" 		} 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJob", - "metadata": { 	- "name": "llama3-lora-finetune", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "datasets": [ 		- { 			- "name": "alpaca-train", 			- "type": "training" 			} 		], 	- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 	- "displayName": "Sprint 3 SFT Run", 	- "peft": { 		- "loraAlpha": 1, 		- "loraDropout": "string", 		- "loraR": 1, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true 		}, 	- "resources": { 		- "claims": [ 			- { 				- "name": "string", 				- "request": "string" 				} 			], 		- "limits": { 			- "property1": 0, 			- "property2": 0 			}, 		- "requests": { 			- "property1": 0, 			- "property2": 0 			} 		}, 	- "training": { 		- "baseModel": "llama3-8b-base", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "evalSteps": 20, 		- "fp16": false, 		- "gradientAccumulationSteps": 0, 		- "jobType": "SFT", 		- "learningRate": "2e-4", 		- "learningRateWarmupSteps": 0, 		- "loggingSteps": 1, 		- "maxLength": 0, 		- "numEpochs": 0, 		- "saveIntervalSteps": -1, 		- "seed": 42, 		- "validationSplitPercentage": 10 		}, 	- "workPVC": { 		- "accessModes": [ 			- "string" 			], 		- "claimName": "string", 		- "mountPath": "string", 		- "selector": { 			- "property1": "string", 			- "property2": "string" 			}, 		- "size": "50Gi", 		- "storageClassName": "string", 		- "volumeName": "string" 		} 	}, - "status": { 	- "artifacts": { 		- "adaptersDir": "string", 		- "donePath": "string", 		- "earlyStopPath": "string", 		- "errorPath": "string", 		- "failedPath": "string", 		- "metricsPath": "string", 		- "outputDir": "string", 		- "runConfigPath": "string", 		- "startedPath": "string", 		- "summaryPath": "string", 		- "tensorBoardDir": "string", 		- "workDir": "string" 		}, 	- "completedAt": "2019-08-24T14:15:22Z", 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "duration": "string", 	- "evaluation": { 		- "evalPath": "string", 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "metrics": { 			- "adapterEvalLoss": "string", 			- "adapterPPL": "string", 			- "baselineEvalLoss": "string", 			- "baselinePPL": "string", 			- "deltaEvalLoss": "string", 			- "deltaPPLPercent": "string" 			}, 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "loraAdapterUpload": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "loraAdapterName": "string", 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "message": "string", 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "preprocessing": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "resolvedTrainingParams": { 		- "baseModel": "string", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "epochs": 0, 		- "evalInterval": 0, 		- "fp16": true, 		- "gradientAccumulation": 0, 		- "isCompatible": true, 		- "learningRate": "string", 		- "learningRateWarmupSteps": 0, 		- "loggingInterval": 0, 		- "loraAlpha": 0, 		- "loraDropout": "string", 		- "loraRank": 0, 		- "maxContextLength": 0, 		- "recipeId": "string", 		- "saveInterval": 0, 		- "seed": 0, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true, 		- "validationSplitPercentage": 0 		}, 	- "training": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "validation": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		} 	} }`

## Delete a FineTuningJob

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

## Read the status of a FineTuningJob

Returns the current `status` subresource of the FineTuningJob. The status is managed exclusively by the controller and cannot be updated by clients.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJob", - "metadata": { 	- "name": "llama3-lora-finetune", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "acceleratorClass": "h100-80gb", 	- "datasets": [ 		- { 			- "name": "alpaca-train", 			- "type": "training" 			} 		], 	- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 	- "displayName": "Sprint 3 SFT Run", 	- "peft": { 		- "loraAlpha": 1, 		- "loraDropout": "string", 		- "loraR": 1, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true 		}, 	- "resources": { 		- "claims": [ 			- { 				- "name": "string", 				- "request": "string" 				} 			], 		- "limits": { 			- "property1": 0, 			- "property2": 0 			}, 		- "requests": { 			- "property1": 0, 			- "property2": 0 			} 		}, 	- "training": { 		- "baseModel": "llama3-8b-base", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "evalSteps": 20, 		- "fp16": false, 		- "gradientAccumulationSteps": 0, 		- "jobType": "SFT", 		- "learningRate": "2e-4", 		- "learningRateWarmupSteps": 0, 		- "loggingSteps": 1, 		- "maxLength": 0, 		- "numEpochs": 0, 		- "saveIntervalSteps": -1, 		- "seed": 42, 		- "validationSplitPercentage": 10 		}, 	- "workPVC": { 		- "accessModes": [ 			- "string" 			], 		- "claimName": "string", 		- "mountPath": "string", 		- "selector": { 			- "property1": "string", 			- "property2": "string" 			}, 		- "size": "50Gi", 		- "storageClassName": "string", 		- "volumeName": "string" 		} 	}, - "status": { 	- "artifacts": { 		- "adaptersDir": "string", 		- "donePath": "string", 		- "earlyStopPath": "string", 		- "errorPath": "string", 		- "failedPath": "string", 		- "metricsPath": "string", 		- "outputDir": "string", 		- "runConfigPath": "string", 		- "startedPath": "string", 		- "summaryPath": "string", 		- "tensorBoardDir": "string", 		- "workDir": "string" 		}, 	- "completedAt": "2019-08-24T14:15:22Z", 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "duration": "string", 	- "evaluation": { 		- "evalPath": "string", 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "metrics": { 			- "adapterEvalLoss": "string", 			- "adapterPPL": "string", 			- "baselineEvalLoss": "string", 			- "baselinePPL": "string", 			- "deltaEvalLoss": "string", 			- "deltaPPLPercent": "string" 			}, 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "loraAdapterUpload": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "loraAdapterName": "string", 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "message": "string", 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "preprocessing": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "resolvedTrainingParams": { 		- "baseModel": "string", 		- "batchSize": 0, 		- "bf16": true, 		- "earlyStopping": { 			- "enabled": false, 			- "greaterIsBetter": false, 			- "metric": "eval_loss", 			- "patience": 3, 			- "threshold": "0.0" 			}, 		- "epochs": 0, 		- "evalInterval": 0, 		- "fp16": true, 		- "gradientAccumulation": 0, 		- "isCompatible": true, 		- "learningRate": "string", 		- "learningRateWarmupSteps": 0, 		- "loggingInterval": 0, 		- "loraAlpha": 0, 		- "loraDropout": "string", 		- "loraRank": 0, 		- "maxContextLength": 0, 		- "recipeId": "string", 		- "saveInterval": 0, 		- "seed": 0, 		- "targetModules": [ 			- "string" 			], 		- "useQlora": true, 		- "validationSplitPercentage": 0 		}, 	- "training": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		}, 	- "validation": { 		- "jobRef": { 			- "completedTime": "2019-08-24T14:15:22Z", 			- "createdTime": "2019-08-24T14:15:22Z", 			- "name": "string", 			- "uid": "string" 			}, 		- "message": "string", 		- "phase": "Pending", 		- "result": "Unknown" 		} 	} }`

## List FineTuningJobs across all namespaces

##### Authorizations:

*BearerToken*

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "FineTuningJobList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "FineTuningJob", 		- "metadata": { 			- "name": "llama3-lora-finetune", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "acceleratorClass": "h100-80gb", 			- "datasets": [ 				- { 					- "name": "alpaca-train", 					- "type": "training" 					} 				], 			- "description": "Sprint 3 SFT on alpaca-train with bumped LR.", 			- "displayName": "Sprint 3 SFT Run", 			- "peft": { 				- "loraAlpha": 1, 				- "loraDropout": "string", 				- "loraR": 1, 				- "targetModules": [ 					- "string" 					], 				- "useQlora": true 				}, 			- "resources": { 				- "claims": [ 					- { 						- "name": "string", 						- "request": "string" 						} 					], 				- "limits": { 					- "property1": 0, 					- "property2": 0 					}, 				- "requests": { 					- "property1": 0, 					- "property2": 0 					} 				}, 			- "training": { 				- "baseModel": "llama3-8b-base", 				- "batchSize": 0, 				- "bf16": true, 				- "earlyStopping": { 					- "enabled": false, 					- "greaterIsBetter": false, 					- "metric": "eval_loss", 					- "patience": 3, 					- "threshold": "0.0" 					}, 				- "evalSteps": 20, 				- "fp16": false, 				- "gradientAccumulationSteps": 0, 				- "jobType": "SFT", 				- "learningRate": "2e-4", 				- "learningRateWarmupSteps": 0, 				- "loggingSteps": 1, 				- "maxLength": 0, 				- "numEpochs": 0, 				- "saveIntervalSteps": -1, 				- "seed": 42, 				- "validationSplitPercentage": 10 				}, 			- "workPVC": { 				- "accessModes": [ 					- "string" 					], 				- "claimName": "string", 				- "mountPath": "string", 				- "selector": { 					- "property1": "string", 					- "property2": "string" 					}, 				- "size": "50Gi", 				- "storageClassName": "string", 				- "volumeName": "string" 				} 			}, 		- "status": { 			- "artifacts": { 				- "adaptersDir": "string", 				- "donePath": "string", 				- "earlyStopPath": "string", 				- "errorPath": "string", 				- "failedPath": "string", 				- "metricsPath": "string", 				- "outputDir": "string", 				- "runConfigPath": "string", 				- "startedPath": "string", 				- "summaryPath": "string", 				- "tensorBoardDir": "string", 				- "workDir": "string" 				}, 			- "completedAt": "2019-08-24T14:15:22Z", 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "duration": "string", 			- "evaluation": { 				- "evalPath": "string", 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "message": "string", 				- "metrics": { 					- "adapterEvalLoss": "string", 					- "adapterPPL": "string", 					- "baselineEvalLoss": "string", 					- "baselinePPL": "string", 					- "deltaEvalLoss": "string", 					- "deltaPPLPercent": "string" 					}, 				- "phase": "Pending", 				- "result": "Unknown" 				}, 			- "loraAdapterUpload": { 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "loraAdapterName": "string", 				- "message": "string", 				- "phase": "Pending", 				- "result": "Unknown" 				}, 			- "message": "string", 			- "observedGeneration": 0, 			- "phase": "Pending", 			- "preprocessing": { 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "message": "string", 				- "phase": "Pending", 				- "result": "Unknown" 				}, 			- "resolvedTrainingParams": { 				- "baseModel": "string", 				- "batchSize": 0, 				- "bf16": true, 				- "earlyStopping": { 					- "enabled": false, 					- "greaterIsBetter": false, 					- "metric": "eval_loss", 					- "patience": 3, 					- "threshold": "0.0" 					}, 				- "epochs": 0, 				- "evalInterval": 0, 				- "fp16": true, 				- "gradientAccumulation": 0, 				- "isCompatible": true, 				- "learningRate": "string", 				- "learningRateWarmupSteps": 0, 				- "loggingInterval": 0, 				- "loraAlpha": 0, 				- "loraDropout": "string", 				- "loraRank": 0, 				- "maxContextLength": 0, 				- "recipeId": "string", 				- "saveInterval": 0, 				- "seed": 0, 				- "targetModules": [ 					- "string" 					], 				- "useQlora": true, 				- "validationSplitPercentage": 0 				}, 			- "training": { 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "message": "string", 				- "phase": "Pending", 				- "result": "Unknown" 				}, 			- "validation": { 				- "jobRef": { 					- "completedTime": "2019-08-24T14:15:22Z", 					- "createdTime": "2019-08-24T14:15:22Z", 					- "name": "string", 					- "uid": "string" 					}, 				- "message": "string", 				- "phase": "Pending", 				- "result": "Unknown" 				} 			} 		} 	] }`

## LoRAAdapter

LoRAAdapter represents a LoRA adapter produced by a FineTuningJob. Adapters are stored under a per-model layout in SeaweedFS (/loraadapters/{namespace}/{model}/{adapter-name}) and can be dynamically loaded into a running ModelDeployment via the vLLM load/unload endpoints.

tags here and on Model use the Go 1.24 encoding/json "omitzero" form. Every other v1alpha1 type uses "omitempty". Verify generated CRD OpenAPI matches expectations under both; if not, switch to omitempty for consistency.

## List LoRAAdapters in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "LoRAAdapterList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "LoRAAdapter", 		- "metadata": { 			- "name": "llama3-alpaca-lora", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "dataset": "alpaca-train", 			- "description": "Finance Q&A adapter trained on internal Q3 2026 docs.", 			- "displayName": "Finance Q&A Adapter", 			- "integrity": { 				- "md5": { 					- "property1": "string", 					- "property2": "string" 					} 				}, 			- "model": "llama3-8b-base", 			- "sourceFineTuningJob": "string" 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "files": [ 				- { 					- "path": "string", 					- "size": 0 					} 				], 			- "integrity": { 				- "files": { 					- "property1": { 						- "md5": "string", 						- "size": 0 						}, 					- "property2": { 						- "md5": "string", 						- "size": 0 						} 					} 				}, 			- "observedGeneration": 0, 			- "phase": "Pending", 			- "ready": true, 			- "size": 0, 			- "storageRef": { 				- "path": "string" 				}, 			- "uploadComplete": true, 			- "usedBy": [ 				- "string" 				] 			} 		} 	] }`

## Create a LoRAAdapter in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  spec defines the desired state of LoRAAdapter |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "LoRAAdapter", - "metadata": { 	- "name": "llama3-alpaca-lora", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "dataset": "alpaca-train", 	- "description": "Finance Q&A adapter trained on internal Q3 2026 docs.", 	- "displayName": "Finance Q&A Adapter", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "model": "llama3-8b-base", 	- "sourceFineTuningJob": "string" 	} }`

### Response samples

- 201
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "LoRAAdapter", - "metadata": { 	- "name": "llama3-alpaca-lora", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "dataset": "alpaca-train", 	- "description": "Finance Q&A adapter trained on internal Q3 2026 docs.", 	- "displayName": "Finance Q&A Adapter", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "model": "llama3-8b-base", 	- "sourceFineTuningJob": "string" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "files": { 			- "property1": { 				- "md5": "string", 				- "size": 0 				}, 			- "property2": { 				- "md5": "string", 				- "size": 0 				} 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "ready": true, 	- "size": 0, 	- "storageRef": { 		- "path": "string" 		}, 	- "uploadComplete": true, 	- "usedBy": [ 		- "string" 		] 	} }`

## Read a LoRAAdapter

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "LoRAAdapter", - "metadata": { 	- "name": "llama3-alpaca-lora", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "dataset": "alpaca-train", 	- "description": "Finance Q&A adapter trained on internal Q3 2026 docs.", 	- "displayName": "Finance Q&A Adapter", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "model": "llama3-8b-base", 	- "sourceFineTuningJob": "string" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "files": { 			- "property1": { 				- "md5": "string", 				- "size": 0 				}, 			- "property2": { 				- "md5": "string", 				- "size": 0 				} 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "ready": true, 	- "size": 0, 	- "storageRef": { 		- "path": "string" 		}, 	- "uploadComplete": true, 	- "usedBy": [ 		- "string" 		] 	} }`

## Delete a LoRAAdapter

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

## Read the status of a LoRAAdapter

Returns the current `status` subresource of the LoRAAdapter. The status is managed exclusively by the controller and cannot be updated by clients.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "LoRAAdapter", - "metadata": { 	- "name": "llama3-alpaca-lora", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "dataset": "alpaca-train", 	- "description": "Finance Q&A adapter trained on internal Q3 2026 docs.", 	- "displayName": "Finance Q&A Adapter", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "model": "llama3-8b-base", 	- "sourceFineTuningJob": "string" 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "files": { 			- "property1": { 				- "md5": "string", 				- "size": 0 				}, 			- "property2": { 				- "md5": "string", 				- "size": 0 				} 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "ready": true, 	- "size": 0, 	- "storageRef": { 		- "path": "string" 		}, 	- "uploadComplete": true, 	- "usedBy": [ 		- "string" 		] 	} }`

## Upload a file to a LoRAAdapter

Uploads a single file to the LoRAAdapter's storage directory in SeaweedFS, scoped to the base ModelClass the adapter targets. The front proxy routes the request based on the `x-upload-target` header.

To upload an entire adapter directory (config + weight shards), call this endpoint once per file, preserving the relative path in `{filePath}`.

After all files are uploaded, the LoRAAdapter controller verifies file presence and updates `status` accordingly.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| modelClass  required | string  Name of the base ModelClass the LoRA adapter targets. The front proxy uses this segment to route the upload to the correct storage prefix. |
| name  required | string  Name of the resource. |
| filePath  required | string  Remote file path within the artifact's storage directory. When uploading a directory tree, this preserves the relative path structure (e.g. `subdir/data.parquet`). May contain forward slashes for nested paths; the Envoy front proxy handles the full path via regex routing. |

##### header Parameters

| x-upload-target  required | string  Value: "loraadapters"  Must be set to `loraadapters` for LoRA adapter file uploads. |
| --- | --- |
| Content-MD5 | string  Example: d0e972641a9148f265e5ec218f1fc3cc  Hex-encoded MD5 digest of the file being uploaded. When provided, the server verifies the uploaded file's integrity against this value during upload. For Model and Dataset uploads, corresponds to the `spec.integrity.md5` field on the resource. |

##### Request Body schema: multipart/form-datarequired

Single-file upload as multipart/form-data. The `file` part carries the raw file content.

| file  required | string \<binary>  The file content to upload. |
| --- | --- |

### Responses

## List LoRAAdapters across all namespaces

##### Authorizations:

*BearerToken*

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "LoRAAdapterList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "LoRAAdapter", 		- "metadata": { 			- "name": "llama3-alpaca-lora", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "dataset": "alpaca-train", 			- "description": "Finance Q&A adapter trained on internal Q3 2026 docs.", 			- "displayName": "Finance Q&A Adapter", 			- "integrity": { 				- "md5": { 					- "property1": "string", 					- "property2": "string" 					} 				}, 			- "model": "llama3-8b-base", 			- "sourceFineTuningJob": "string" 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "files": [ 				- { 					- "path": "string", 					- "size": 0 					} 				], 			- "integrity": { 				- "files": { 					- "property1": { 						- "md5": "string", 						- "size": 0 						}, 					- "property2": { 						- "md5": "string", 						- "size": 0 						} 					} 				}, 			- "observedGeneration": 0, 			- "phase": "Pending", 			- "ready": true, 			- "size": 0, 			- "storageRef": { 				- "path": "string" 				}, 			- "uploadComplete": true, 			- "usedBy": [ 				- "string" 				] 			} 		} 	] }`

## Model

Model represents a stored or remotely-sourced AI model artifact within a namespace. It carries descriptive metadata about the model (family, type, precision, quantization, parameter count, etc.) and acts as the central identity that ModelClass, LoRAAdapter, and FineTuningJob reference.

rackai.rackspace.com/uri-hash label with the following rules:

- Controller service account (e.g. rackai-controller-manager) MAY add, update, or remove the label. The controller stamps it when cache=true is first reconciled and removes it during the cache=true→false cleanup path.
- All other principals (end-users, CI, kubectl) MUST NOT modify or delete the label once it has been stamped. Reject the request with a clear message explaining that the label is managed by the controller.

A webhook is necessary here because CEL transition rules apply to ALL mutations regardless of who makes them, so CEL cannot distinguish the controller from a user and would block legitimate controller cleanup.

## List Models in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "Model", 		- "metadata": { 			- "name": "llama3-8b-base", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "authors": [ 				- "string" 				], 			- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 			- "displayName": "LLaMA 3.1 8B Instruct", 			- "integrity": { 				- "md5": { 					- "property1": "string", 					- "property2": "string" 					} 				}, 			- "languages": [ 				- "string" 				], 			- "modelFamily": "LLaMA", 			- "parameterCount": "7B", 			- "precision": "FP16", 			- "quantization": "none", 			- "source": { 				- "cache": true, 				- "modelPullCredential": "hf-modelpull-token", 				- "type": "Upload", 				- "uri": "hf://qwen/qwen3-4b" 				}, 			- "tasks": [ 				- "string" 				] 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "files": [ 				- { 					- "path": "string", 					- "size": 0 					} 				], 			- "integrity": { 				- "md5": { 					- "property1": "string", 					- "property2": "string" 					} 				}, 			- "observedGeneration": 0, 			- "phase": "Pending", 			- "pvName": "string", 			- "pvcName": "string", 			- "ready": true, 			- "size": 0 			} 		} 	] }`

## Create a Model in a namespace

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of Model. |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Model", - "metadata": { 	- "name": "llama3-8b-base", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "authors": [ 		- "string" 		], 	- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 	- "displayName": "LLaMA 3.1 8B Instruct", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "languages": [ 		- "string" 		], 	- "modelFamily": "LLaMA", 	- "parameterCount": "7B", 	- "precision": "FP16", 	- "quantization": "none", 	- "source": { 		- "cache": true, 		- "modelPullCredential": "hf-modelpull-token", 		- "type": "Upload", 		- "uri": "hf://qwen/qwen3-4b" 		}, 	- "tasks": [ 		- "string" 		] 	} }`

### Response samples

- 201
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Model", - "metadata": { 	- "name": "llama3-8b-base", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "authors": [ 		- "string" 		], 	- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 	- "displayName": "LLaMA 3.1 8B Instruct", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "languages": [ 		- "string" 		], 	- "modelFamily": "LLaMA", 	- "parameterCount": "7B", 	- "precision": "FP16", 	- "quantization": "none", 	- "source": { 		- "cache": true, 		- "modelPullCredential": "hf-modelpull-token", 		- "type": "Upload", 		- "uri": "hf://qwen/qwen3-4b" 		}, 	- "tasks": [ 		- "string" 		] 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "pvName": "string", 	- "pvcName": "string", 	- "ready": true, 	- "size": 0 	} }`

## Read a Model

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Model", - "metadata": { 	- "name": "llama3-8b-base", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "authors": [ 		- "string" 		], 	- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 	- "displayName": "LLaMA 3.1 8B Instruct", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "languages": [ 		- "string" 		], 	- "modelFamily": "LLaMA", 	- "parameterCount": "7B", 	- "precision": "FP16", 	- "quantization": "none", 	- "source": { 		- "cache": true, 		- "modelPullCredential": "hf-modelpull-token", 		- "type": "Upload", 		- "uri": "hf://qwen/qwen3-4b" 		}, 	- "tasks": [ 		- "string" 		] 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "pvName": "string", 	- "pvcName": "string", 	- "ready": true, 	- "size": 0 	} }`

## Replace a Model

Replaces the full Model object. The following spec fields are **immutable** after creation and must match the existing values: `spec.source.type`, `spec.source.uri`.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of Model. |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Model", - "metadata": { 	- "name": "llama3-8b-base", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "authors": [ 		- "string" 		], 	- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 	- "displayName": "LLaMA 3.1 8B Instruct", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "languages": [ 		- "string" 		], 	- "modelFamily": "LLaMA", 	- "parameterCount": "7B", 	- "precision": "FP16", 	- "quantization": "none", 	- "source": { 		- "cache": true, 		- "modelPullCredential": "hf-modelpull-token", 		- "type": "Upload", 		- "uri": "hf://qwen/qwen3-4b" 		}, 	- "tasks": [ 		- "string" 		] 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Model", - "metadata": { 	- "name": "llama3-8b-base", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "authors": [ 		- "string" 		], 	- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 	- "displayName": "LLaMA 3.1 8B Instruct", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "languages": [ 		- "string" 		], 	- "modelFamily": "LLaMA", 	- "parameterCount": "7B", 	- "precision": "FP16", 	- "quantization": "none", 	- "source": { 		- "cache": true, 		- "modelPullCredential": "hf-modelpull-token", 		- "type": "Upload", 		- "uri": "hf://qwen/qwen3-4b" 		}, 	- "tasks": [ 		- "string" 		] 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "pvName": "string", 	- "pvcName": "string", 	- "ready": true, 	- "size": 0 	} }`

## Partially update a Model

Applies a JSON merge-patch to the Model. The following spec fields are **immutable** after creation and cannot be changed by a patch: `spec.source.type`, `spec.source.uri`. Attempts to modify them are rejected by the Kubernetes API server with a 422 response.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/merge-patch+jsonrequired

| apiVersion | string  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources) |
| --- | --- |
| kind | string  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds) |
| metadata | object  metadata is a standard object metadata. More info: [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata) |
| spec  required | object  Spec defines the desired state of Model. |

### Responses

### Request samples

- Payload
Content type

application/merge-patch+json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Model", - "metadata": { 	- "name": "llama3-8b-base", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "authors": [ 		- "string" 		], 	- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 	- "displayName": "LLaMA 3.1 8B Instruct", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "languages": [ 		- "string" 		], 	- "modelFamily": "LLaMA", 	- "parameterCount": "7B", 	- "precision": "FP16", 	- "quantization": "none", 	- "source": { 		- "cache": true, 		- "modelPullCredential": "hf-modelpull-token", 		- "type": "Upload", 		- "uri": "hf://qwen/qwen3-4b" 		}, 	- "tasks": [ 		- "string" 		] 	} }`

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Model", - "metadata": { 	- "name": "llama3-8b-base", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "authors": [ 		- "string" 		], 	- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 	- "displayName": "LLaMA 3.1 8B Instruct", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "languages": [ 		- "string" 		], 	- "modelFamily": "LLaMA", 	- "parameterCount": "7B", 	- "precision": "FP16", 	- "quantization": "none", 	- "source": { 		- "cache": true, 		- "modelPullCredential": "hf-modelpull-token", 		- "type": "Upload", 		- "uri": "hf://qwen/qwen3-4b" 		}, 	- "tasks": [ 		- "string" 		] 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "pvName": "string", 	- "pvcName": "string", 	- "ready": true, 	- "size": 0 	} }`

## Delete a Model

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

## Read the status of a Model

Returns the current `status` subresource of the Model. The status is managed exclusively by the controller and cannot be updated by clients.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "Model", - "metadata": { 	- "name": "llama3-8b-base", 	- "namespace": "org-idxxxxxxxxxx" 	}, - "spec": { 	- "authors": [ 		- "string" 		], 	- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 	- "displayName": "LLaMA 3.1 8B Instruct", 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "languages": [ 		- "string" 		], 	- "modelFamily": "LLaMA", 	- "parameterCount": "7B", 	- "precision": "FP16", 	- "quantization": "none", 	- "source": { 		- "cache": true, 		- "modelPullCredential": "hf-modelpull-token", 		- "type": "Upload", 		- "uri": "hf://qwen/qwen3-4b" 		}, 	- "tasks": [ 		- "string" 		] 	}, - "status": { 	- "conditions": [ 		- { 			- "lastTransitionTime": "2019-08-24T14:15:22Z", 			- "message": "string", 			- "observedGeneration": 0, 			- "reason": "string", 			- "status": "True", 			- "type": "string" 			} 		], 	- "files": [ 		- { 			- "path": "string", 			- "size": 0 			} 		], 	- "integrity": { 		- "md5": { 			- "property1": "string", 			- "property2": "string" 			} 		}, 	- "observedGeneration": 0, 	- "phase": "Pending", 	- "pvName": "string", 	- "pvcName": "string", 	- "ready": true, 	- "size": 0 	} }`

## Upload a file to a Model

Uploads a single file to the Model's storage directory in SeaweedFS. The front proxy routes this request based on the `x-upload-target` header.

To upload an entire model directory, call this endpoint once per file, preserving the relative path in the `{filePath}` parameter.

After all files are uploaded, the Model controller verifies file presence, computes total size, and (if configured) checks MD5 integrity, then sets `status.ready = true`.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |
| filePath  required | string  Remote file path within the artifact's storage directory. When uploading a directory tree, this preserves the relative path structure (e.g. `subdir/data.parquet`). May contain forward slashes for nested paths; the Envoy front proxy handles the full path via regex routing. |

##### header Parameters

| x-upload-target  required | string  Value: "models"  Must be set to `models` for model file uploads. |
| --- | --- |
| Content-MD5 | string  Example: d0e972641a9148f265e5ec218f1fc3cc  Hex-encoded MD5 digest of the file being uploaded. When provided, the server verifies the uploaded file's integrity against this value during upload. For Model and Dataset uploads, corresponds to the `spec.integrity.md5` field on the resource. |

##### Request Body schema: multipart/form-datarequired

Single-file upload as multipart/form-data. The `file` part carries the raw file content.

| file  required | string \<binary>  The file content to upload. |
| --- | --- |

### Responses

## List Models across all namespaces

##### Authorizations:

*BearerToken*

##### query Parameters

| labelSelector | string  Selector to restrict the list of returned objects by their labels. Defaults to everything. |
| --- | --- |
| fieldSelector | string  Selector to restrict the list of returned objects by their fields. Defaults to everything. |
| limit | integer >= 1  Maximum number of responses to return for a list call. The server may return fewer results than requested. |
| continue | string  Opaque token returned by a previous list call to continue pagination. |

### Responses

### Response samples

- 200
Content type

application/json

`{ - "apiVersion": "rackai.rackspace.com/v1alpha1", - "kind": "ModelList", - "metadata": { }, - "items": [ 	- { 		- "apiVersion": "rackai.rackspace.com/v1alpha1", 		- "kind": "Model", 		- "metadata": { 			- "name": "llama3-8b-base", 			- "namespace": "org-idxxxxxxxxxx" 			}, 		- "spec": { 			- "authors": [ 				- "string" 				], 			- "description": "LLaMA 3.1 8B Instruct, original FP16 weights from Meta.", 			- "displayName": "LLaMA 3.1 8B Instruct", 			- "integrity": { 				- "md5": { 					- "property1": "string", 					- "property2": "string" 					} 				}, 			- "languages": [ 				- "string" 				], 			- "modelFamily": "LLaMA", 			- "parameterCount": "7B", 			- "precision": "FP16", 			- "quantization": "none", 			- "source": { 				- "cache": true, 				- "modelPullCredential": "hf-modelpull-token", 				- "type": "Upload", 				- "uri": "hf://qwen/qwen3-4b" 				}, 			- "tasks": [ 				- "string" 				] 			}, 		- "status": { 			- "conditions": [ 				- { 					- "lastTransitionTime": "2019-08-24T14:15:22Z", 					- "message": "string", 					- "observedGeneration": 0, 					- "reason": "string", 					- "status": "True", 					- "type": "string" 					} 				], 			- "files": [ 				- { 					- "path": "string", 					- "size": 0 					} 				], 			- "integrity": { 				- "md5": { 					- "property1": "string", 					- "property2": "string" 					} 				}, 			- "observedGeneration": 0, 			- "phase": "Pending", 			- "pvName": "string", 			- "pvcName": "string", 			- "ready": true, 			- "size": 0 			} 		} 	] }`

## Inference

OpenAI-compatible inference requests, proxied to the engine serving a ModelDeployment.

## Create a text completion

Proxies an OpenAI-compatible text-completion request to the engine serving the named ModelDeployment. The request and response bodies are defined by the engine (vLLM / NIM); only the common fields are shown here. To target a loaded LoRA adapter, set `model` to the adapter's served name.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/jsonrequired

| model  required | string  Served model name, or a loaded LoRA adapter's served name. |
| --- | --- |
| prompt  required | string |
| max\_tokens | integer |
| temperature | number |
| stream | boolean |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "model": "phoenix", - "prompt": "Write a haiku about GPUs.", - "max_tokens": 128, - "temperature": 0.7, - "stream": false }`

### Response samples

- 200
Content type

application/json

`{ - "id": "cmpl-xxxxxxxx", - "object": "text_completion", - "model": "phoenix", - "choices": [ 	- { 		- "index": 0, 		- "text": "string", 		- "finish_reason": "stop" 		} 	] }`

## Create a chat completion

Proxies an OpenAI-compatible chat-completion request to the engine serving the named ModelDeployment. The request and response bodies are defined by the engine (vLLM / NIM); only the common fields are shown here. To target a loaded LoRA adapter, set `model` to the adapter's served name.

##### Authorizations:

*BearerToken*

##### path Parameters

| namespace  required | string  Kubernetes namespace of the resource. |
| --- | --- |
| name  required | string  Name of the resource. |

##### Request Body schema: application/jsonrequired

| model  required | string  Served model name, or a loaded LoRA adapter's served name. |
| --- | --- |
| messages  required | Array of objects |
| max\_tokens | integer |
| temperature | number |
| stream | boolean |

### Responses

### Request samples

- Payload
Content type

application/json

`{ - "model": "phoenix", - "messages": [], - "max_tokens": 256, - "temperature": 0.7, - "stream": false }`

### Response samples

- 200
Content type

application/json

`{}`