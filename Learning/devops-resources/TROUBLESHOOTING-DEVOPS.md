# 🔧 Troubleshooting Guide

Common issues and solutions for Docker, Kubernetes, and AWS.

---

## 🐳 Docker Troubleshooting

### Issue: Docker Desktop Won't Start

**Symptoms:**
- Docker Desktop crashes on startup
- "Docker is starting..." never completes

**Solutions:**

1. **Restart Docker Desktop**
```bash
# Windows (PowerShell as Admin)
Restart-Service docker

# Mac
killall Docker && open /Applications/Docker.app

# Linux
sudo systemctl restart docker
```

2. **Clear Docker Data**
```bash
# Windows: Docker Desktop → Troubleshoot → Clean/Purge data
# Mac: Docker Desktop → Bug icon → Clean/Purge data

# Or manually (Linux)
sudo rm -rf /var/lib/docker
sudo systemctl restart docker
```

3. **Check WSL2 (Windows)**
```bash
wsl --list --verbose
wsl --set-default-version 2
wsl --update
```

---

### Issue: Container Won't Start

**Symptoms:**
- Container exits immediately
- Status shows "Exited (1)"

**Diagnosis:**
```bash
# View container logs
docker logs <container-id>

# Check exit code
docker ps -a

# Inspect container
docker inspect <container-id>
```

**Common Causes:**

1. **Missing or wrong command**
```dockerfile
# Wrong - no process to keep container running
FROM ubuntu

# Right - long-running process
FROM ubuntu
CMD ["tail", "-f", "/dev/null"]
```

2. **Application error**
```bash
# Check application logs
docker logs <container-id>

# Run interactively to debug
docker run -it myapp bash
```

3. **Port already in use**
```bash
# Check what's using the port
netstat -ano | findstr :8080  # Windows
lsof -i :8080                  # Mac/Linux

# Use different port
docker run -p 8081:80 nginx
```

---

### Issue: Cannot Connect to Container

**Symptoms:**
- localhost:port not accessible
- Connection refused

**Solutions:**

1. **Check port mapping**
```bash
# Wrong - no port mapping
docker run nginx

# Right - port mapping
docker run -p 8080:80 nginx

# Verify port mapping
docker port <container-id>
```

2. **Check container is running**
```bash
docker ps
# If not running, check logs
docker logs <container-id>
```

3. **Check firewall**
```bash
# Windows Firewall
# Settings → Windows Security → Firewall → Allow an app

# Linux
sudo ufw allow 8080
sudo iptables -L
```

---

### Issue: Image Build Fails

**Symptoms:**
- "ERROR: failed to solve"
- Build hangs or times out

**Solutions:**

1. **Check Dockerfile syntax**
```dockerfile
# Wrong - FROM must be first
WORKDIR /app
FROM node:16

# Right
FROM node:16
WORKDIR /app
```

2. **Clear build cache**
```bash
docker build --no-cache -t myapp .
```

3. **Check network connectivity**
```bash
# Test if you can reach registry
ping docker.io

# Use proxy if needed
docker build --build-arg HTTP_PROXY=http://proxy:8080 .
```

4. **Check disk space**
```bash
# Check space
docker system df

# Clean up
docker system prune -a
```

---

### Issue: "no space left on device"

**Solutions:**

```bash
# Check disk usage
docker system df

# Remove unused containers
docker container prune

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune

# Remove everything
docker system prune -a --volumes

# Check Docker disk space (Mac/Windows)
# Docker Desktop → Settings → Resources → Disk image size
```

---

### Issue: Permission Denied (Linux)

**Symptoms:**
- "permission denied while trying to connect to Docker daemon"

**Solutions:**

```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in, or:
newgrp docker

# Verify
docker ps
```

---

### Issue: Slow Build Times

**Solutions:**

1. **Use .dockerignore**
```
# .dockerignore
node_modules
.git
*.log
.env
```

2. **Order Dockerfile efficiently**
```dockerfile
# Wrong - invalidates cache on any code change
COPY . .
RUN npm install

# Right - cache dependencies separately
COPY package*.json ./
RUN npm install
COPY . .
```

3. **Use multi-stage builds**
```dockerfile
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:16-alpine
COPY --from=builder /app/dist ./dist
CMD ["node", "dist/index.js"]
```

---

## ☸️ Kubernetes Troubleshooting

### Issue: Pod Stuck in Pending

**Symptoms:**
- Pod status: Pending
- Pod never starts

**Diagnosis:**
```bash
# Check pod events
kubectl describe pod <pod-name>

# Check node resources
kubectl top nodes
kubectl describe nodes
```

**Common Causes:**

1. **Insufficient resources**
```bash
# Check resource requests
kubectl get pod <pod-name> -o yaml | grep -A 5 resources

# Solution: Lower resource requests or add nodes
```

2. **No available nodes**
```bash
# Check node status
kubectl get nodes

# Check node conditions
kubectl describe node <node-name>
```

3. **Volume mount issues**
```bash
# Check PVC status
kubectl get pvc

# Describe PVC
kubectl describe pvc <pvc-name>
```

---

### Issue: Pod Stuck in CrashLoopBackOff

**Symptoms:**
- Pod keeps restarting
- Status: CrashLoopBackOff

**Diagnosis:**
```bash
# Check logs
kubectl logs <pod-name>
kubectl logs <pod-name> --previous

# Check events
kubectl describe pod <pod-name>

# Check pod details
kubectl get pod <pod-name> -o yaml
```

**Common Causes:**

1. **Application error**
```bash
# Check application logs
kubectl logs <pod-name> -f

# Exec into container (if it stays up long enough)
kubectl exec -it <pod-name> -- bash
```

2. **Missing environment variables**
```yaml
# Add env vars or ConfigMap
env:
  - name: DATABASE_URL
    value: "postgresql://db:5432/myapp"
```

3. **Failed health checks**
```yaml
# Adjust probes
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30  # Give app time to start
  periodSeconds: 10
```

---

### Issue: Service Not Accessible

**Symptoms:**
- Cannot reach service
- Connection timeout

**Diagnosis:**
```bash
# Check service
kubectl get svc
kubectl describe svc <service-name>

# Check endpoints
kubectl get endpoints <service-name>

# Check pods
kubectl get pods -l app=<app-label>
```

**Solutions:**

1. **Check selector labels**
```bash
# Service selector must match pod labels
kubectl get svc <service-name> -o yaml
kubectl get pods --show-labels
```

2. **Check service type**
```yaml
# ClusterIP - internal only
type: ClusterIP

# NodePort - external access
type: NodePort

# LoadBalancer - cloud load balancer
type: LoadBalancer
```

3. **Test connectivity**
```bash
# From another pod
kubectl run test --image=busybox -it --rm -- wget -O- http://service-name

# Port forward to local
kubectl port-forward svc/<service-name> 8080:80
```

---

### Issue: ImagePullBackOff

**Symptoms:**
- Pod status: ImagePullBackOff or ErrImagePull

**Diagnosis:**
```bash
kubectl describe pod <pod-name>
# Look for events about image pull
```

**Common Causes:**

1. **Image doesn't exist**
```bash
# Check image name
kubectl get pod <pod-name> -o yaml | grep image:

# Verify image exists
docker pull <image-name>
```

2. **Authentication required**
```bash
# Create docker registry secret
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<username> \
  --docker-password=<password>

# Use in pod
spec:
  imagePullSecrets:
  - name: regcred
```

3. **Wrong registry**
```yaml
# Make sure registry is correct
image: docker.io/library/nginx:latest
# or
image: gcr.io/project/image:tag
```

---

### Issue: Cannot Delete Namespace

**Symptoms:**
- Namespace stuck in "Terminating"
- `kubectl delete namespace` hangs

**Solutions:**

```bash
# Check what's blocking deletion
kubectl api-resources --verbs=list --namespaced -o name \
  | xargs -n 1 kubectl get --show-kind --ignore-not-found -n <namespace>

# Force delete
kubectl delete namespace <namespace> --grace-period=0 --force

# If still stuck, remove finalizers
kubectl get namespace <namespace> -o json \
  | jq '.spec.finalizers = []' \
  | kubectl replace --raw /api/v1/namespaces/<namespace>/finalize -f -
```

---

### Issue: kubectl Commands Slow

**Solutions:**

```bash
# Increase timeout
kubectl get pods --request-timeout=10s

# Check cluster connectivity
kubectl cluster-info

# Check API server
kubectl get --raw /healthz

# Clear cache
rm -rf ~/.kube/cache
```

---

### Issue: ConfigMap/Secret Not Updating in Pod

**Symptoms:**
- Updated ConfigMap/Secret not reflected in pod

**Solution:**

```bash
# ConfigMaps and Secrets are not automatically updated
# You need to restart pods

# Restart deployment
kubectl rollout restart deployment <deployment-name>

# Or delete pods (if managed by deployment)
kubectl delete pod -l app=<app-label>
```

---

## ☁️ AWS Troubleshooting

### Issue: Cannot Connect to EC2 Instance

**Symptoms:**
- SSH connection timeout
- Connection refused

**Diagnosis:**
```bash
# Test connectivity
ping <public-ip>
telnet <public-ip> 22

# Check instance status
aws ec2 describe-instance-status --instance-ids <instance-id>
```

**Common Causes:**

1. **Security Group issues**
```bash
# Check security groups
aws ec2 describe-security-groups --group-ids <sg-id>

# Allow SSH from your IP
aws ec2 authorize-security-group-ingress \
  --group-id <sg-id> \
  --protocol tcp \
  --port 22 \
  --cidr <your-ip>/32
```

2. **Wrong key pair**
```bash
# Make sure you're using the right key
ssh -i correct-key.pem ec2-user@<ip>

# Check key permissions
chmod 400 key.pem
```

3. **Instance stopped**
```bash
# Check instance state
aws ec2 describe-instances --instance-ids <instance-id>

# Start instance
aws ec2 start-instances --instance-ids <instance-id>
```

---

### Issue: EC2 Instance Not Starting

**Symptoms:**
- Instance stuck in "pending"
- Status checks failing

**Solutions:**

```bash
# Check system logs
aws ec2 get-console-output --instance-id <instance-id>

# Check limits
aws ec2 describe-account-attributes

# Check instance health
aws ec2 describe-instance-status --instance-ids <instance-id>
```

---

### Issue: S3 Access Denied

**Symptoms:**
- "Access Denied" when accessing S3
- 403 Forbidden

**Solutions:**

1. **Check bucket policy**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::bucket-name/*"
    }
  ]
}
```

2. **Check IAM permissions**
```bash
# List your permissions
aws iam get-user-policy --user-name <username> --policy-name <policy-name>

# Attach S3 full access (for testing)
aws iam attach-user-policy \
  --user-name <username> \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```

3. **Check bucket ACL**
```bash
aws s3api get-bucket-acl --bucket <bucket-name>
```

---

### Issue: RDS Connection Timeout

**Symptoms:**
- Cannot connect to RDS
- Connection timeout

**Solutions:**

1. **Check security group**
```bash
# Allow connection from your IP
aws rds modify-db-instance \
  --db-instance-identifier <db-name> \
  --vpc-security-group-ids <sg-id>

# Security group must allow port 5432 (PostgreSQL) or 3306 (MySQL)
```

2. **Check public accessibility**
```bash
# Make DB publicly accessible (not recommended for production)
aws rds modify-db-instance \
  --db-instance-identifier <db-name> \
  --publicly-accessible
```

3. **Test connection**
```bash
# PostgreSQL
psql -h <endpoint> -U <username> -d <database>

# MySQL
mysql -h <endpoint> -u <username> -p
```

---

### Issue: IAM Permission Denied

**Symptoms:**
- "User is not authorized to perform..."
- Access Denied errors

**Diagnosis:**
```bash
# Check current user
aws sts get-caller-identity

# Check attached policies
aws iam list-attached-user-policies --user-name <username>
```

**Solutions:**

```bash
# Attach required policy
aws iam attach-user-policy \
  --user-name <username> \
  --policy-arn <policy-arn>

# Create custom policy
aws iam create-policy \
  --policy-name MyPolicy \
  --policy-document file://policy.json
```

---

### Issue: EKS Cluster Won't Create

**Symptoms:**
- Cluster creation fails
- Stuck in "Creating"

**Solutions:**

```bash
# Check CloudFormation stacks
aws cloudformation describe-stacks

# Check cluster status
aws eks describe-cluster --name <cluster-name>

# Check IAM role
aws iam get-role --role-name <eks-role-name>

# Delete and recreate
aws eks delete-cluster --name <cluster-name>
```

---

### Issue: High AWS Bills

**Symptoms:**
- Unexpected charges
- Cost alerts

**Diagnosis:**
```bash
# Check cost and usage
aws ce get-cost-and-usage \
  --time-period Start=2024-01-01,End=2024-01-31 \
  --granularity MONTHLY \
  --metrics BlendedCost

# Use Cost Explorer in AWS Console
```

**Common Causes:**

1. **Running resources**
```bash
# Check running EC2 instances
aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,State.Name]'

# Stop instances
aws ec2 stop-instances --instance-ids <id>

# Check NAT Gateways (expensive!)
aws ec2 describe-nat-gateways

# Check Load Balancers
aws elbv2 describe-load-balancers
```

2. **Storage costs**
```bash
# Check EBS volumes
aws ec2 describe-volumes

# Delete unused volumes
aws ec2 delete-volume --volume-id <vol-id>

# Check S3 storage
aws s3 ls --summarize --recursive s3://bucket-name
```

3. **Data transfer**
- Moving data between regions
- Internet data transfer
- Use CloudFront CDN

---

## 🔍 General Debugging Tips

### 1. Check Logs First

```bash
# Docker
docker logs <container-id>

# Kubernetes
kubectl logs <pod-name>

# AWS
aws logs tail /aws/lambda/<function-name> --follow
```

### 2. Use Verbose Output

```bash
# Docker
docker build --progress=plain .

# Kubernetes
kubectl apply -f manifest.yaml -v=9

# AWS
aws ec2 describe-instances --debug
```

### 3. Validate Configuration

```bash
# Docker Compose
docker-compose config

# Kubernetes
kubectl apply --dry-run=client -f manifest.yaml

# AWS CloudFormation
aws cloudformation validate-template --template-body file://template.yaml
```

### 4. Test Connectivity

```bash
# Basic network test
ping <host>
telnet <host> <port>
curl -v http://<host>:<port>

# DNS resolution
nslookup <hostname>
dig <hostname>

# Inside container
docker exec -it <container> ping <host>
kubectl exec -it <pod> -- curl <service-name>
```

### 5. Check Resource Usage

```bash
# Docker
docker stats

# Kubernetes
kubectl top nodes
kubectl top pods

# System
top
htop
free -m
df -h
```

---

## 📝 Debugging Checklist

When something doesn't work:

- [ ] Check logs/events
- [ ] Verify configuration syntax
- [ ] Test connectivity/network
- [ ] Check permissions/security groups
- [ ] Verify resources exist
- [ ] Check resource usage
- [ ] Google the error message
- [ ] Check official documentation
- [ ] Ask in community forums

---

## 🆘 Getting Help

### Before Asking for Help

1. **Search first**
   - Google the error
   - Check Stack Overflow
   - Read documentation

2. **Gather information**
   - Error messages
   - Configuration files
   - Commands you ran
   - System information

3. **Create minimal reproduction**
   - Simplify to smallest failing example
   - Remove unrelated code

### When Asking for Help

**Good Question:**
```
I'm trying to deploy a Node.js app to Kubernetes. The pod is crashing
with "Error: Cannot find module 'express'". 

My Dockerfile:
FROM node:16
WORKDIR /app
COPY . .
CMD ["node", "server.js"]

My deployment.yaml:
[paste relevant parts]

I've tried:
- Rebuilding the image
- Checking the image has node_modules

Error logs:
[paste logs]

What am I missing?
```

**Bad Question:**
```
My app doesn't work. Help!
```

---

## 🔗 Useful Resources

- [Docker Troubleshooting](https://docs.docker.com/config/daemon/)
- [Kubernetes Troubleshooting](https://kubernetes.io/docs/tasks/debug/)
- [AWS Support](https://aws.amazon.com/premiumsupport/)
- [Stack Overflow](https://stackoverflow.com/)

---

**Remember:** Everyone faces these issues. Don't get discouraged! Debugging is a skill that improves with practice. 💪

