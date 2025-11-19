# ☸️ Kubernetes Beginner Guide

## What is Kubernetes?

Kubernetes (K8s) is an open-source container orchestration platform that automates deploying, scaling, and managing containerized applications.

### Why Kubernetes?

**Docker alone is great, but:**
- How do you manage 100+ containers?
- How do you handle container failures?
- How do you scale automatically?
- How do you update without downtime?

**Kubernetes solves these problems!**
- ✅ Automatic container scheduling
- ✅ Self-healing (restarts failed containers)
- ✅ Horizontal scaling
- ✅ Load balancing
- ✅ Rolling updates and rollbacks
- ✅ Service discovery
- ✅ Secret management

---

## 🏗️ Kubernetes Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CONTROL PLANE                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  API Server  │  │  Scheduler   │  │  Controller  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │              etcd (Cluster State)                │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   NODE 1    │   │   NODE 2    │   │   NODE 3    │
│ ┌─────────┐ │   │ ┌─────────┐ │   │ ┌─────────┐ │
│ │ Kubelet │ │   │ │ Kubelet │ │   │ │ Kubelet │ │
│ └─────────┘ │   │ └─────────┘ │   │ └─────────┘ │
│ ┌─────────┐ │   │ ┌─────────┐ │   │ ┌─────────┐ │
│ │  Pods   │ │   │ │  Pods   │ │   │ │  Pods   │ │
│ └─────────┘ │   │ └─────────┘ │   │ └─────────┘ │
└─────────────┘   └─────────────┘   └─────────────┘
```

### Control Plane Components

- **API Server:** Front-end for Kubernetes control plane
- **etcd:** Key-value store for cluster data
- **Scheduler:** Assigns pods to nodes
- **Controller Manager:** Maintains desired state

### Node Components

- **Kubelet:** Agent that runs on each node
- **Container Runtime:** Docker, containerd, etc.
- **Kube-proxy:** Network proxy

---

## 🧱 Core Kubernetes Objects

### 1. Pod
- Smallest deployable unit
- One or more containers
- Shares network and storage
- Ephemeral (can be replaced)

### 2. Deployment
- Manages ReplicaSets
- Declares desired state
- Handles rolling updates
- Most common way to run apps

### 3. Service
- Stable network endpoint
- Load balances across pods
- Service discovery
- Types: ClusterIP, NodePort, LoadBalancer

### 4. Namespace
- Virtual clusters
- Resource isolation
- Multi-tenancy

---

## 🚀 Installation

### Local Development Options

#### 1. Minikube (Recommended for Learning)

```bash
# Windows
choco install minikube

# macOS
brew install minikube

# Linux
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Start minikube
minikube start

# Check status
minikube status

# Open dashboard
minikube dashboard
```

#### 2. Docker Desktop
- Enable Kubernetes in Docker Desktop settings
- Easiest option if you already have Docker Desktop

#### 3. Kind (Kubernetes in Docker)

```bash
# Install
brew install kind  # macOS
choco install kind # Windows

# Create cluster
kind create cluster --name my-cluster

# Delete cluster
kind delete cluster --name my-cluster
```

### Install kubectl (Kubernetes CLI)

```bash
# Windows
choco install kubernetes-cli

# macOS
brew install kubectl

# Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Verify installation
kubectl version --client
```

---

## 📝 Essential kubectl Commands

### Cluster Info

```bash
# Check cluster info
kubectl cluster-info

# View nodes
kubectl get nodes

# Describe node
kubectl describe node <node-name>

# Check cluster health
kubectl get componentstatuses
```

### Working with Pods

```bash
# List pods
kubectl get pods

# List pods with more info
kubectl get pods -o wide

# List pods in all namespaces
kubectl get pods --all-namespaces
kubectl get pods -A

# Describe pod
kubectl describe pod <pod-name>

# Create pod from YAML
kubectl apply -f pod.yaml

# Delete pod
kubectl delete pod <pod-name>

# View pod logs
kubectl logs <pod-name>

# Follow logs
kubectl logs -f <pod-name>

# Execute command in pod
kubectl exec -it <pod-name> -- bash

# Port forward to pod
kubectl port-forward <pod-name> 8080:80
```

### Working with Deployments

```bash
# List deployments
kubectl get deployments

# Create deployment
kubectl create deployment nginx --image=nginx

# Apply from YAML
kubectl apply -f deployment.yaml

# Scale deployment
kubectl scale deployment nginx --replicas=3

# Update image
kubectl set image deployment/nginx nginx=nginx:1.21

# Rollout status
kubectl rollout status deployment/nginx

# Rollout history
kubectl rollout history deployment/nginx

# Rollback
kubectl rollout undo deployment/nginx

# Delete deployment
kubectl delete deployment nginx
```

### Working with Services

```bash
# List services
kubectl get services
kubectl get svc

# Expose deployment
kubectl expose deployment nginx --port=80 --type=LoadBalancer

# Apply service from YAML
kubectl apply -f service.yaml

# Describe service
kubectl describe service nginx

# Delete service
kubectl delete service nginx
```

### Namespaces

```bash
# List namespaces
kubectl get namespaces
kubectl get ns

# Create namespace
kubectl create namespace dev

# Set default namespace
kubectl config set-context --current --namespace=dev

# List resources in namespace
kubectl get all -n dev

# Delete namespace
kubectl delete namespace dev
```

---

## 📄 YAML Manifests

Kubernetes uses YAML files to define objects.

### Pod YAML

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
```

### Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
```

### Service YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer
```

---

## 🎯 Hands-On Exercise: Deploy Your First App

### Step 1: Create a Deployment

**deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
```

```bash
# Apply the deployment
kubectl apply -f deployment.yaml

# Check deployment
kubectl get deployments

# Check pods
kubectl get pods

# Watch pods being created
kubectl get pods -w
```

### Step 2: Expose with a Service

**service.yaml**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: NodePort
```

```bash
# Apply the service
kubectl apply -f service.yaml

# Check service
kubectl get services

# Get service URL (Minikube)
minikube service web-service --url

# Or port forward
kubectl port-forward service/web-service 8080:80
```

### Step 3: Scale the Application

```bash
# Scale to 5 replicas
kubectl scale deployment web-app --replicas=5

# Watch pods scaling
kubectl get pods -w

# Scale back to 2
kubectl scale deployment web-app --replicas=2
```

### Step 4: Update the Application

```bash
# Update the image
kubectl set image deployment/web-app nginx=nginx:latest

# Watch rollout
kubectl rollout status deployment/web-app

# Check rollout history
kubectl rollout history deployment/web-app
```

### Step 5: Rollback

```bash
# Rollback to previous version
kubectl rollout undo deployment/web-app

# Rollback to specific revision
kubectl rollout undo deployment/web-app --to-revision=1
```

### Step 6: Cleanup

```bash
# Delete everything
kubectl delete deployment web-app
kubectl delete service web-service

# Or delete from files
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

---

## 🔍 Understanding Labels and Selectors

Labels are key-value pairs attached to objects.

```yaml
metadata:
  labels:
    app: myapp
    tier: frontend
    environment: production
```

### Using Labels

```bash
# Get pods with specific label
kubectl get pods -l app=myapp

# Get pods with multiple labels
kubectl get pods -l app=myapp,tier=frontend

# Get all resources with label
kubectl get all -l app=myapp

# Add label to existing pod
kubectl label pod my-pod version=v1

# Remove label
kubectl label pod my-pod version-
```

---

## 🎓 Practice Projects

### Project 1: Multi-Container Pod

Create a pod with nginx and a sidecar container:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    ports:
    - containerPort: 80
  - name: sidecar
    image: busybox
    command: ['sh', '-c', 'while true; do echo "Sidecar running"; sleep 10; done']
```

### Project 2: Complete Web App

Deploy a web application with:
- Frontend deployment (3 replicas)
- Backend deployment (2 replicas)
- Services for both
- Proper labels and selectors

### Project 3: Namespace Organization

Create namespaces for:
- Development
- Staging
- Production

Deploy the same app to each namespace.

---

## ⚠️ Common Beginner Mistakes

1. **Not using labels correctly**
   - Labels in deployment template must match selector

2. **Forgetting resource limits**
   - Always set CPU and memory limits

3. **Not checking logs**
   - Use `kubectl logs` to debug issues

4. **Mixing imperative and declarative**
   - Prefer YAML files (declarative) for production

5. **Not understanding pod lifecycle**
   - Pods are ephemeral, data doesn't persist

---

## 🔧 Useful kubectl Shortcuts

```bash
# Aliases
alias k=kubectl
alias kgp='kubectl get pods'
alias kgs='kubectl get services'
alias kgd='kubectl get deployments'

# Quick pod run
kubectl run test --image=nginx --rm -it -- bash

# Get all resources
kubectl get all

# Explain resources
kubectl explain pod
kubectl explain pod.spec.containers

# Create from file and watch
kubectl apply -f app.yaml && kubectl get pods -w

# Delete all in namespace
kubectl delete all --all -n namespace-name
```

---

## 📚 Understanding Service Types

### ClusterIP (Default)
- Internal access only
- Pods can reach via service name
- Not accessible from outside

```yaml
type: ClusterIP
```

### NodePort
- Exposes on each node's IP
- Accessible via NodeIP:NodePort
- Port range: 30000-32767

```yaml
type: NodePort
```

### LoadBalancer
- Creates external load balancer
- Cloud provider integration
- Gets external IP

```yaml
type: LoadBalancer
```

### ExternalName
- Maps to DNS name
- For external services

```yaml
type: ExternalName
externalName: api.example.com
```

---

## ✅ Beginner Checklist

- [ ] Kubernetes installed (Minikube/Kind)
- [ ] kubectl installed and configured
- [ ] Understand Pods, Deployments, Services
- [ ] Can create resources from YAML
- [ ] Can scale deployments
- [ ] Understand labels and selectors
- [ ] Can view logs and exec into pods
- [ ] Can update and rollback deployments
- [ ] Understand different service types
- [ ] Comfortable with kubectl commands

---

## 🚀 Next Steps

Congratulations! You've learned Kubernetes basics.

Move to: `kubernetes/02-intermediate/`

**Next Topics:**
- ConfigMaps and Secrets
- Persistent Volumes
- StatefulSets
- Ingress
- Advanced networking

