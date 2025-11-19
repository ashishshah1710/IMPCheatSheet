# ☸️ Kubernetes (kubectl) Cheat Sheet

## Cluster Management

```bash
# Cluster info
kubectl cluster-info
kubectl cluster-info dump

# View cluster nodes
kubectl get nodes
kubectl get nodes -o wide
kubectl describe node <node-name>

# Check cluster health
kubectl get componentstatuses
kubectl get cs

# View API versions
kubectl api-versions

# View API resources
kubectl api-resources
```

## Context and Configuration

```bash
# View contexts
kubectl config get-contexts
kubectl config current-context

# Switch context
kubectl config use-context <context-name>

# Set default namespace
kubectl config set-context --current --namespace=dev

# View config
kubectl config view

# Set credentials
kubectl config set-credentials user1 --token=abc123
```

## Pod Management

```bash
# List pods
kubectl get pods
kubectl get pods -o wide
kubectl get pods --all-namespaces
kubectl get pods -A
kubectl get pods -n <namespace>

# Describe pod
kubectl describe pod <pod-name>

# Create pod
kubectl run nginx --image=nginx
kubectl run busybox --image=busybox --restart=Never -- sleep 3600

# Apply from YAML
kubectl apply -f pod.yaml

# Delete pod
kubectl delete pod <pod-name>
kubectl delete -f pod.yaml

# View logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>                  # Follow
kubectl logs <pod-name> -c <container>      # Multi-container
kubectl logs --previous <pod-name>          # Previous instance
kubectl logs --since=1h <pod-name>          # Last hour
kubectl logs --tail=50 <pod-name>           # Last 50 lines

# Execute commands
kubectl exec <pod-name> -- ls
kubectl exec -it <pod-name> -- bash
kubectl exec -it <pod-name> -c <container> -- bash

# Port forwarding
kubectl port-forward <pod-name> 8080:80
kubectl port-forward pod/<pod-name> 8080:80

# Copy files
kubectl cp <pod-name>:/path/file ./file
kubectl cp ./file <pod-name>:/path/file

# Pod status
kubectl get pods --field-selector=status.phase=Running
kubectl get pods --field-selector=status.phase=Failed
```

## Deployment Management

```bash
# Create deployment
kubectl create deployment nginx --image=nginx
kubectl create deployment nginx --image=nginx --replicas=3

# List deployments
kubectl get deployments
kubectl get deploy
kubectl get deployment <name> -o yaml

# Describe deployment
kubectl describe deployment <name>

# Apply deployment
kubectl apply -f deployment.yaml

# Scale deployment
kubectl scale deployment <name> --replicas=5
kubectl scale deployment <name> --replicas=0

# Autoscale
kubectl autoscale deployment <name> --min=2 --max=10 --cpu-percent=80

# Update image
kubectl set image deployment/<name> container=nginx:1.21
kubectl set image deployment/<name> *=nginx:1.21  # All containers

# Rollout status
kubectl rollout status deployment/<name>

# Rollout history
kubectl rollout history deployment/<name>
kubectl rollout history deployment/<name> --revision=2

# Rollback
kubectl rollout undo deployment/<name>
kubectl rollout undo deployment/<name> --to-revision=2

# Pause/Resume rollout
kubectl rollout pause deployment/<name>
kubectl rollout resume deployment/<name>

# Restart deployment
kubectl rollout restart deployment/<name>

# Delete deployment
kubectl delete deployment <name>
```

## Service Management

```bash
# List services
kubectl get services
kubectl get svc
kubectl get svc -o wide

# Describe service
kubectl describe service <name>

# Create service
kubectl expose deployment <name> --port=80 --target-port=8080
kubectl expose deployment <name> --port=80 --type=LoadBalancer
kubectl expose deployment <name> --port=80 --type=NodePort

# Apply service
kubectl apply -f service.yaml

# Get service URL (Minikube)
minikube service <service-name> --url

# Get endpoints
kubectl get endpoints <service-name>

# Delete service
kubectl delete service <name>
```

## Namespace Management

```bash
# List namespaces
kubectl get namespaces
kubectl get ns

# Create namespace
kubectl create namespace dev

# Apply from YAML
kubectl apply -f namespace.yaml

# Delete namespace
kubectl delete namespace dev

# Get resources in namespace
kubectl get all -n dev
kubectl get pods -n dev

# Set default namespace
kubectl config set-context --current --namespace=dev
```

## ConfigMap and Secrets

```bash
# ConfigMaps
kubectl create configmap my-config --from-literal=key1=value1
kubectl create configmap my-config --from-file=config.properties
kubectl create configmap my-config --from-env-file=.env
kubectl get configmaps
kubectl get configmap my-config -o yaml
kubectl describe configmap my-config
kubectl delete configmap my-config

# Secrets
kubectl create secret generic my-secret --from-literal=password=abc123
kubectl create secret generic my-secret --from-file=ssh-key=~/.ssh/id_rsa
kubectl create secret docker-registry regcred \
  --docker-server=registry.io \
  --docker-username=user \
  --docker-password=pass
kubectl get secrets
kubectl get secret my-secret -o yaml
kubectl describe secret my-secret
kubectl delete secret my-secret

# Decode secret
kubectl get secret my-secret -o jsonpath='{.data.password}' | base64 -d
```

## Labels and Selectors

```bash
# Add label
kubectl label pods <pod-name> env=prod
kubectl label pods <pod-name> tier=frontend

# Remove label
kubectl label pods <pod-name> env-

# Update label
kubectl label pods <pod-name> env=staging --overwrite

# Filter by label
kubectl get pods -l env=prod
kubectl get pods -l env=prod,tier=frontend
kubectl get pods -l 'env in (prod,staging)'
kubectl get pods -l env!=dev

# Show labels
kubectl get pods --show-labels
kubectl get pods -L env,tier
```

## Annotations

```bash
# Add annotation
kubectl annotate pods <pod-name> description="My application"

# Remove annotation
kubectl annotate pods <pod-name> description-

# View annotations
kubectl describe pod <pod-name>
```

## Resource Management

```bash
# Get all resources
kubectl get all
kubectl get all -n <namespace>
kubectl get all --all-namespaces

# Get multiple resource types
kubectl get pods,services,deployments

# Get with custom output
kubectl get pods -o wide
kubectl get pods -o yaml
kubectl get pods -o json
kubectl get pods -o name

# Get with JSONPath
kubectl get pods -o jsonpath='{.items[*].metadata.name}'
kubectl get pods -o jsonpath='{.items[*].status.podIP}'

# Get with custom columns
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase

# Sort
kubectl get pods --sort-by=.metadata.creationTimestamp
kubectl get pods --sort-by=.status.startTime

# Watch resources
kubectl get pods -w
kubectl get pods --watch

# Diff before apply
kubectl diff -f deployment.yaml
```

## Node Management

```bash
# Get nodes
kubectl get nodes
kubectl get nodes -o wide

# Describe node
kubectl describe node <node-name>

# Cordon node (mark unschedulable)
kubectl cordon <node-name>

# Drain node (evict pods)
kubectl drain <node-name> --ignore-daemonsets

# Uncordon node
kubectl uncordon <node-name>

# Node labels
kubectl label nodes <node-name> disktype=ssd

# Taint node
kubectl taint nodes <node-name> key=value:NoSchedule
kubectl taint nodes <node-name> key=value:NoExecute

# Remove taint
kubectl taint nodes <node-name> key-
```

## YAML Templates

### Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: myapp
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
    env:
    - name: ENV_VAR
      value: "production"
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

### Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
  labels:
    app: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: myapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer
```

### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  database_url: "postgresql://localhost:5432/mydb"
  api_key: "abc123"
  config.json: |
    {
      "env": "production",
      "debug": false
    }
```

### Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: YWRtaW4=  # base64 encoded
  password: cGFzc3dvcmQ=
```

## Persistent Volumes

```bash
# PersistentVolume
kubectl get pv
kubectl describe pv <pv-name>

# PersistentVolumeClaim
kubectl get pvc
kubectl describe pvc <pvc-name>
kubectl delete pvc <pvc-name>

# StorageClass
kubectl get storageclass
kubectl get sc
kubectl describe sc <sc-name>
```

### PVC YAML

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: standard
```

## Ingress

```bash
# Get ingress
kubectl get ingress
kubectl get ing
kubectl describe ingress <name>

# Apply ingress
kubectl apply -f ingress.yaml

# Delete ingress
kubectl delete ingress <name>
```

### Ingress YAML

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              number: 80
```

## Jobs and CronJobs

```bash
# Jobs
kubectl get jobs
kubectl describe job <name>
kubectl delete job <name>

# CronJobs
kubectl get cronjobs
kubectl get cj
kubectl describe cronjob <name>
kubectl delete cronjob <name>
```

### Job YAML

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: my-job
spec:
  template:
    spec:
      containers:
      - name: task
        image: busybox
        command: ["echo", "Hello Kubernetes!"]
      restartPolicy: Never
  backoffLimit: 4
```

### CronJob YAML

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: my-cronjob
spec:
  schedule: "0 */4 * * *"  # Every 4 hours
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: task
            image: busybox
            command: ["echo", "Scheduled task"]
          restartPolicy: OnFailure
```

## RBAC (Role-Based Access Control)

```bash
# ServiceAccounts
kubectl get serviceaccounts
kubectl get sa
kubectl create serviceaccount my-sa

# Roles
kubectl get roles
kubectl describe role <name>

# RoleBindings
kubectl get rolebindings
kubectl describe rolebinding <name>

# ClusterRoles
kubectl get clusterroles

# ClusterRoleBindings
kubectl get clusterrolebindings
```

## Resource Quotas and Limits

```bash
# ResourceQuota
kubectl get resourcequotas
kubectl get quota
kubectl describe quota <name>

# LimitRange
kubectl get limitranges
kubectl get limits
kubectl describe limits <name>
```

## Events and Troubleshooting

```bash
# View events
kubectl get events
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl get events --field-selector type=Warning
kubectl get events -n <namespace>

# Describe for events
kubectl describe pod <pod-name>
kubectl describe node <node-name>

# Top (requires metrics-server)
kubectl top nodes
kubectl top pods
kubectl top pods -n <namespace>
kubectl top pods --all-namespaces

# Debugging pods
kubectl get pods --field-selector=status.phase=Failed
kubectl logs <pod-name> --previous
kubectl describe pod <pod-name>
kubectl get pod <pod-name> -o yaml
```

## Advanced Operations

```bash
# Apply with prune (delete removed resources)
kubectl apply -f . --prune -l app=myapp

# Server-side apply
kubectl apply -f deployment.yaml --server-side

# Replace (delete and recreate)
kubectl replace -f deployment.yaml --force

# Patch
kubectl patch deployment <name> -p '{"spec":{"replicas":5}}'

# Edit resource
kubectl edit deployment <name>

# Set resources
kubectl set resources deployment <name> -c=nginx --limits=cpu=500m,memory=512Mi

# Set env
kubectl set env deployment/<name> ENV_VAR=value

# Create from URL
kubectl apply -f https://example.com/manifest.yaml

# Dry run
kubectl apply -f deployment.yaml --dry-run=client
kubectl apply -f deployment.yaml --dry-run=server

# Explain resources
kubectl explain pod
kubectl explain pod.spec
kubectl explain pod.spec.containers

# Wait for condition
kubectl wait --for=condition=Ready pod/<pod-name>
kubectl wait --for=delete pod/<pod-name> --timeout=60s
```

## Aliases

```bash
# Add to ~/.bashrc or ~/.zshrc

alias k='kubectl'
alias kg='kubectl get'
alias kd='kubectl describe'
alias kdel='kubectl delete'
alias ka='kubectl apply -f'
alias kex='kubectl exec -it'
alias klog='kubectl logs -f'
alias kgp='kubectl get pods'
alias kgs='kubectl get services'
alias kgd='kubectl get deployments'
alias kgn='kubectl get nodes'
alias kga='kubectl get all'
alias kctx='kubectl config use-context'
alias kns='kubectl config set-context --current --namespace'

# Enable autocomplete
source <(kubectl completion bash)
# Or for zsh
source <(kubectl completion zsh)
```

## Quick Reference Table

| Resource | Short Name | Command |
|----------|-----------|---------|
| pods | po | `kubectl get po` |
| services | svc | `kubectl get svc` |
| deployments | deploy | `kubectl get deploy` |
| replicasets | rs | `kubectl get rs` |
| statefulsets | sts | `kubectl get sts` |
| daemonsets | ds | `kubectl get ds` |
| jobs | | `kubectl get jobs` |
| cronjobs | cj | `kubectl get cj` |
| configmaps | cm | `kubectl get cm` |
| secrets | | `kubectl get secrets` |
| namespaces | ns | `kubectl get ns` |
| nodes | no | `kubectl get no` |
| persistentvolumes | pv | `kubectl get pv` |
| persistentvolumeclaims | pvc | `kubectl get pvc` |
| ingress | ing | `kubectl get ing` |

## Common Patterns

```bash
# Create and expose deployment
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer

# Quick pod for testing
kubectl run test --image=busybox --rm -it --restart=Never -- sh

# Debug networking
kubectl run test-net --image=nicolaka/netshoot --rm -it -- bash

# View all resources in namespace
kubectl get all -n production

# Delete all pods matching label
kubectl delete pods -l app=myapp

# Get pod IP addresses
kubectl get pods -o wide | awk '{print $1, $6}'

# Restart all pods in deployment
kubectl rollout restart deployment/myapp

# Scale all deployments
kubectl scale deployment --all --replicas=0
```

## Best Practices

```yaml
# Always specify resource limits
resources:
  requests:
    memory: "64Mi"
    cpu: "250m"
  limits:
    memory: "128Mi"
    cpu: "500m"

# Use readiness and liveness probes
livenessProbe:
  httpGet:
    path: /health
    port: 8080
readinessProbe:
  httpGet:
    path: /ready
    port: 8080

# Use specific image tags
image: nginx:1.21.0  # Not 'latest'

# Label everything
metadata:
  labels:
    app: myapp
    version: "1.0"
    environment: production
```

---

**Pro Tip:** Use `kubectl explain` to understand any resource!

```bash
kubectl explain pod.spec.containers.resources.limits
```

