# 🐳 Docker - Advanced Level

Master Docker for production environments and enterprise deployments!

---

## 📚 Table of Contents

1. [Multi-Stage Builds](#multi-stage-builds)
2. [Docker Security](#docker-security)
3. [Docker Networking Advanced](#docker-networking)
4. [Performance Optimization](#performance-optimization)
5. [Docker in Production](#docker-production)
6. [Docker Swarm vs Kubernetes](#orchestration)
7. [CI/CD with Docker](#cicd-docker)
8. [Interview Questions](#interview-questions)

---

## 🏗️ Multi-Stage Builds

### Optimized Production Builds

```dockerfile
# Stage 1: Build Stage
FROM maven:3.8-openjdk-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Runtime Stage
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]

# Result: Build artifacts not included in final image
# Final image size: ~200MB vs ~800MB single-stage
```

### Node.js Multi-Stage Build

```dockerfile
# Stage 1: Dependencies
FROM node:18-alpine AS dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Stage 2: Build
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 3: Production
FROM node:18-alpine AS production
WORKDIR /app
COPY --from=dependencies /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
COPY package.json ./
EXPOSE 3000
USER node
CMD ["node", "dist/index.js"]
```

---

## 🔒 Docker Security

### Security Best Practices

```dockerfile
# 1. Use specific image versions (not latest)
FROM node:18.17.0-alpine3.18

# 2. Run as non-root user
RUN addgroup -g 1001 appgroup && \
    adduser -D -u 1001 -G appgroup appuser
USER appuser

# 3. Use COPY instead of ADD
COPY --chown=appuser:appgroup . /app

# 4. Scan for vulnerabilities
# docker scan myimage:latest
# trivy image myimage:latest

# 5. Use .dockerignore
# .git
# node_modules
# *.md
# .env

# 6. Minimize layers and attack surface
RUN apk add --no-cache \
    ca-certificates \
    && rm -rf /var/cache/apk/*

# 7. Use read-only root filesystem
# docker run --read-only myimage

# 8. Set resource limits
# docker run --memory="512m" --cpus="1.0" myimage

# 9. Use secrets for sensitive data
# docker secret create db_password password.txt
# docker service create --secret db_password myimage

# 10. Enable content trust
# export DOCKER_CONTENT_TRUST=1
```

### Security Scanning Example

```bash
# Install Trivy
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Scan image
trivy image node:18-alpine

# Scan filesystem
trivy fs --security-checks vuln,config .

# Scan with specific severity
trivy image --severity HIGH,CRITICAL myapp:latest

# Generate report
trivy image --format json --output report.json myapp:latest
```

---

## 🌐 Docker Networking Advanced

### Custom Bridge Networks

```bash
# Create custom network
docker network create --driver bridge \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1 \
  mynetwork

# Create with options
docker network create \
  --driver bridge \
  --opt "com.docker.network.bridge.name"="docker1" \
  --opt "com.docker.network.driver.mtu"="1450" \
  mynetwork

# Connect container to multiple networks
docker run -d --name web \
  --network frontend \
  --network backend \
  nginx

# Disconnect/Connect on running container
docker network disconnect frontend web
docker network connect frontend web
```

### Host and Overlay Networks

```bash
# Host network (no isolation)
docker run --network host nginx

# Overlay network (for Swarm)
docker network create --driver overlay \
  --attachable \
  --subnet=10.0.0.0/24 \
  overlay-network

# MacVLAN network (assign MAC address)
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 \
  macvlan-network
```

---

## ⚡ Performance Optimization

### Image Optimization Techniques

```dockerfile
# 1. Use Alpine base images
FROM python:3.11-alpine

# 2. Combine RUN commands
RUN apk add --no-cache gcc musl-dev libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del gcc musl-dev libffi-dev

# 3. Order layers by change frequency
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# 4. Use BuildKit cache mounts
# syntax=docker/dockerfile:1
FROM python:3.11
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# 5. Leverage .dockerignore
# node_modules
# .git
# *.md
# tests/

# 6. Multi-stage builds to reduce size
FROM node:18 AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

### BuildKit Features

```bash
# Enable BuildKit
export DOCKER_BUILDKIT=1

# Build with cache
docker build --cache-from myapp:latest -t myapp:new .

# Build with secrets
docker build --secret id=aws,src=$HOME/.aws/credentials .

# Build with SSH agent
docker build --ssh default .

# Parallel builds
docker build --build-arg BUILDKIT_INLINE_CACHE=1 .
```

### Resource Limits

```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    image: myapp
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 2G
        reservations:
          cpus: '1.0'
          memory: 1G
    
    # Or with docker run
    # docker run \
    #   --cpus="1.5" \
    #   --memory="2g" \
    #   --memory-swap="3g" \
    #   --memory-reservation="1g" \
    #   --kernel-memory="500m" \
    #   --pids-limit=200 \
    #   myapp
```

---

## 🏭 Docker in Production

### Health Checks

```dockerfile
# Dockerfile health check
FROM node:18-alpine
WORKDIR /app
COPY . .

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node healthcheck.js

# Or in docker-compose.yml
services:
  web:
    image: myapp
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### Logging Best Practices

```bash
# Use json-file driver with rotation
docker run -d \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  myapp

# Send logs to syslog
docker run -d \
  --log-driver syslog \
  --log-opt syslog-address=tcp://192.168.0.42:514 \
  myapp

# Use fluentd
docker run -d \
  --log-driver fluentd \
  --log-opt fluentd-address=localhost:24224 \
  --log-opt tag="docker.{{.Name}}" \
  myapp
```

### Docker Compose Production Setup

```yaml
version: '3.8'

services:
  web:
    image: myapp:${VERSION:-latest}
    restart: unless-stopped
    ports:
      - "80:8080"
    environment:
      - NODE_ENV=production
      - DB_HOST=${DB_HOST}
    env_file:
      - .env.production
    volumes:
      - app-data:/app/data
    networks:
      - frontend
      - backend
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        failure_action: rollback
      resources:
        limits:
          cpus: '2'
          memory: 2G
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  db:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - backend

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - backend

volumes:
  app-data:
  postgres-data:
  redis-data:

networks:
  frontend:
  backend:
    internal: true

secrets:
  db_password:
    external: true
```

---

## 🎯 Docker Swarm

### Swarm Setup and Management

```bash
# Initialize swarm
docker swarm init --advertise-addr 192.168.1.10

# Join worker node
docker swarm join --token SWMTKN-1-xxx 192.168.1.10:2377

# Deploy stack
docker stack deploy -c docker-compose.yml myapp

# Scale service
docker service scale myapp_web=5

# Update service (zero downtime)
docker service update \
  --image myapp:v2 \
  --update-parallelism 2 \
  --update-delay 10s \
  myapp_web

# Rolling back
docker service rollback myapp_web

# Drain node for maintenance
docker node update --availability drain node-1

# Activate node
docker node update --availability active node-1
```

### Production Stack Example

```yaml
version: '3.8'

services:
  web:
    image: myapp:${VERSION}
    ports:
      - "80:8080"
    deploy:
      replicas: 6
      update_config:
        parallelism: 2
        delay: 10s
        failure_action: rollback
        monitor: 60s
      rollback_config:
        parallelism: 2
        delay: 10s
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
        window: 120s
      placement:
        constraints:
          - node.role == worker
          - node.labels.type == web
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    networks:
      - frontend
      - backend
    secrets:
      - source: app_secret
        target: /run/secrets/app_secret
        mode: 0400
    configs:
      - source: app_config
        target: /app/config.yml
```

---

## 🚀 CI/CD with Docker

### GitLab CI/CD Pipeline

```yaml
# .gitlab-ci.yml
variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA

stages:
  - build
  - test
  - push
  - deploy

before_script:
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY

build:
  stage: build
  script:
    - docker build --cache-from $CI_REGISTRY_IMAGE:latest -t $IMAGE_TAG .
    - docker tag $IMAGE_TAG $CI_REGISTRY_IMAGE:latest
  only:
    - main
    - develop

test:
  stage: test
  script:
    - docker run --rm $IMAGE_TAG npm test
    - docker run --rm $IMAGE_TAG npm run lint
  only:
    - main
    - develop

push:
  stage: push
  script:
    - docker push $IMAGE_TAG
    - docker push $CI_REGISTRY_IMAGE:latest
  only:
    - main

deploy_production:
  stage: deploy
  script:
    - docker stack deploy -c docker-compose.prod.yml myapp
  environment:
    name: production
    url: https://myapp.com
  only:
    - main
  when: manual
```

### GitHub Actions Workflow

```yaml
# .github/workflows/docker-build.yml
name: Docker Build and Push

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Log in to Container Registry
        uses: docker/login-action@v2
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha

      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=registry,ref=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:buildcache
          cache-to: type=registry,ref=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:buildcache,mode=max

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ steps.meta.outputs.version }}
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy results to GitHub Security
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'
```

---

## 🎯 Interview Questions

### Advanced Docker Scenarios

**Q1: How do you optimize Docker images for production?**

**Answer:**
1. Use multi-stage builds
2. Use Alpine or distroless base images
3. Minimize layers
4. Order instructions by change frequency
5. Use .dockerignore
6. Don't install unnecessary packages
7. Clean up in the same layer
8. Use COPY instead of ADD
9. Leverage build cache
10. Run as non-root user

**Q2: Explain Docker networking in depth**

**Answer:**
- **Bridge:** Default, isolated network
- **Host:** No isolation, uses host network stack
- **Overlay:** Multi-host networking for Swarm
- **Macvlan:** Assign MAC addresses to containers
- **None:** No networking
- Custom networks provide DNS resolution, isolation, and better control

**Q3: Docker vs VM - Architecture differences**

**Answer:**
- **VM:** Full OS, hypervisor, slower startup, more resource-intensive
- **Docker:** Shared kernel, container runtime, fast startup, lightweight
- Containers share host OS kernel, VMs have separate OS
- Containers better for microservices, VMs for complete isolation

---

**Master Docker for enterprise production systems!** 🚀

