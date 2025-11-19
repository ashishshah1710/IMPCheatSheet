# 🐳 Docker Cheat Sheet

## Container Management

```bash
# Run a container
docker run nginx
docker run -d nginx                         # Detached mode
docker run -it ubuntu bash                  # Interactive
docker run --name my-app nginx              # With name
docker run -p 8080:80 nginx                 # Port mapping
docker run -v $(pwd):/app nginx             # Volume mount
docker run -e NODE_ENV=production node      # Environment variable
docker run --rm nginx                       # Auto-remove after exit

# List containers
docker ps                                   # Running containers
docker ps -a                                # All containers
docker ps -q                                # Only IDs

# Container operations
docker start <container>                    # Start stopped container
docker stop <container>                     # Stop running container
docker restart <container>                  # Restart container
docker pause <container>                    # Pause container
docker unpause <container>                  # Unpause container
docker kill <container>                     # Force stop
docker rm <container>                       # Remove container
docker rm -f <container>                    # Force remove running container

# Container info
docker logs <container>                     # View logs
docker logs -f <container>                  # Follow logs
docker logs --tail 100 <container>          # Last 100 lines
docker inspect <container>                  # Detailed info
docker top <container>                      # Running processes
docker stats                                # Resource usage
docker stats <container>                    # Specific container stats

# Execute commands
docker exec <container> ls                  # Run command
docker exec -it <container> bash            # Interactive shell
docker cp <container>:/path ./local         # Copy from container
docker cp ./local <container>:/path         # Copy to container
```

## Image Management

```bash
# Image operations
docker images                               # List images
docker images -a                            # All images (including intermediate)
docker pull nginx                           # Pull image
docker pull nginx:1.21                      # Specific version
docker push myuser/myapp:tag                # Push to registry
docker rmi <image>                          # Remove image
docker rmi -f <image>                       # Force remove
docker tag myapp myuser/myapp:v1            # Tag image

# Build images
docker build -t myapp:latest .              # Build from Dockerfile
docker build -t myapp:v1 -f Dockerfile.dev .  # Specific Dockerfile
docker build --no-cache -t myapp .          # Build without cache
docker build --build-arg VERSION=1.0 .      # With build arguments

# Image info
docker history <image>                      # Image layers
docker inspect <image>                      # Detailed info
docker search nginx                         # Search Docker Hub
```

## Dockerfile Commands

```dockerfile
# Base image
FROM ubuntu:20.04
FROM python:3.9-slim

# Metadata
LABEL maintainer="email@example.com"
LABEL version="1.0"

# Set working directory
WORKDIR /app

# Copy files
COPY . .
COPY src/ /app/
ADD archive.tar.gz /app/                    # Supports extraction

# Run commands
RUN apt-get update && apt-get install -y python3
RUN pip install -r requirements.txt

# Environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Expose port (documentation only)
EXPOSE 80
EXPOSE 443

# Create mount point
VOLUME /data

# Change user
USER appuser

# Default command (can be overridden)
CMD ["python", "app.py"]
CMD ["npm", "start"]

# Entrypoint (not easily overridden)
ENTRYPOINT ["python"]
CMD ["app.py"]  # Default argument to ENTRYPOINT

# Build arguments
ARG VERSION=1.0
RUN echo "Building version ${VERSION}"
```

## Docker Compose

```bash
# Start services
docker-compose up                           # Start all services
docker-compose up -d                        # Detached mode
docker-compose up --build                   # Build images first
docker-compose up service1 service2         # Specific services

# Stop services
docker-compose down                         # Stop and remove containers
docker-compose down -v                      # Also remove volumes
docker-compose stop                         # Stop without removing
docker-compose stop service1                # Stop specific service

# Service operations
docker-compose start                        # Start stopped services
docker-compose restart                      # Restart services
docker-compose pause                        # Pause services
docker-compose unpause                      # Unpause services

# View info
docker-compose ps                           # List services
docker-compose logs                         # View logs
docker-compose logs -f                      # Follow logs
docker-compose logs service1                # Specific service
docker-compose top                          # Running processes

# Execute commands
docker-compose exec service1 bash           # Interactive shell
docker-compose run service1 command         # Run one-off command

# Build and manage
docker-compose build                        # Build images
docker-compose build --no-cache             # Build without cache
docker-compose pull                         # Pull images
docker-compose push                         # Push images

# Scale services
docker-compose up -d --scale web=3          # Run 3 instances of web
```

## docker-compose.yml Template

```yaml
version: '3.8'

services:
  web:
    build: .                                # Build from Dockerfile
    # OR
    image: nginx:alpine                     # Use existing image
    container_name: my-web
    ports:
      - "80:80"                             # Host:Container
      - "443:443"
    volumes:
      - ./src:/app                          # Bind mount
      - app-data:/data                      # Named volume
    environment:
      - NODE_ENV=production
      - DB_HOST=db
    env_file:
      - .env                                # Load from file
    depends_on:
      - db
    networks:
      - app-network
    restart: unless-stopped                 # Restart policy
    command: npm start                      # Override CMD

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  app-data:
  postgres-data:

networks:
  app-network:
    driver: bridge
```

## Networking

```bash
# List networks
docker network ls

# Create network
docker network create my-network
docker network create --driver bridge my-network

# Inspect network
docker network inspect my-network

# Connect container to network
docker network connect my-network container1

# Disconnect
docker network disconnect my-network container1

# Remove network
docker network rm my-network

# Run container on network
docker run -d --name app1 --network my-network nginx
```

## Volume Management

```bash
# List volumes
docker volume ls

# Create volume
docker volume create my-data

# Inspect volume
docker volume inspect my-data

# Remove volume
docker volume rm my-data

# Remove unused volumes
docker volume prune

# Use volume
docker run -v my-data:/data nginx           # Named volume
docker run -v $(pwd):/app nginx             # Bind mount
docker run -v /app/node_modules nginx       # Anonymous volume
```

## Registry & Image Distribution

```bash
# Docker Hub
docker login                                # Login
docker logout                               # Logout
docker push myuser/myapp:tag                # Push image
docker pull myuser/myapp:tag                # Pull image

# Tag for different registries
docker tag myapp myuser/myapp:latest        # Docker Hub
docker tag myapp gcr.io/project/myapp       # Google Container Registry
docker tag myapp 123456.dkr.ecr.us-east-1.amazonaws.com/myapp  # AWS ECR

# Private registry
docker login registry.example.com
docker tag myapp registry.example.com/myapp:v1
docker push registry.example.com/myapp:v1
```

## System Management

```bash
# View system info
docker info                                 # System-wide info
docker version                              # Version info
docker system df                            # Disk usage

# Clean up
docker container prune                      # Remove stopped containers
docker image prune                          # Remove dangling images
docker image prune -a                       # Remove all unused images
docker volume prune                         # Remove unused volumes
docker network prune                        # Remove unused networks
docker system prune                         # Remove all unused objects
docker system prune -a                      # Remove all + unused images
docker system prune -a --volumes            # Remove everything unused

# Events
docker events                               # Real-time events
docker events --filter 'event=start'        # Filter events
```

## Multi-Stage Builds

```dockerfile
# Stage 1: Build
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:16-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --production
CMD ["node", "dist/index.js"]
```

## Health Checks

```dockerfile
# In Dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

# In docker-compose.yml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 30s
  timeout: 3s
  retries: 3
  start_period: 5s
```

## Resource Limits

```bash
# Memory limits
docker run -m 512m nginx                    # Limit to 512MB
docker run --memory="1g" nginx              # 1GB limit

# CPU limits
docker run --cpus="1.5" nginx               # 1.5 CPUs
docker run --cpu-shares=512 nginx           # Relative weight

# Combined
docker run -m 512m --cpus="1" nginx
```

## Debugging

```bash
# View container output
docker logs <container>
docker logs -f <container>                  # Follow
docker logs --tail 50 <container>           # Last 50 lines
docker logs --since 5m <container>          # Last 5 minutes

# Inspect container
docker inspect <container>                  # Full info
docker inspect -f '{{.State.Status}}' <container>  # Specific field
docker inspect -f '{{.NetworkSettings.IPAddress}}' <container>

# Execute commands for debugging
docker exec <container> ps aux              # List processes
docker exec <container> ls -la              # List files
docker exec <container> env                 # View environment
docker exec <container> cat /app/config.yml # View file

# Copy files for inspection
docker cp <container>:/app/logs/error.log ./

# Port mapping
docker port <container>                     # Show port mappings
```

## Security Best Practices

```dockerfile
# Don't run as root
RUN useradd -m -u 1000 appuser
USER appuser

# Use specific versions
FROM python:3.9.16-slim
# Not: FROM python:latest

# Minimize layers
RUN apt-get update && \
    apt-get install -y package1 package2 && \
    rm -rf /var/lib/apt/lists/*

# Scan images
# docker scan myimage:latest

# Don't store secrets in images
# Use environment variables or secrets management
```

## Useful Aliases

```bash
# Add to ~/.bashrc or ~/.zshrc

alias d='docker'
alias dc='docker-compose'
alias dps='docker ps'
alias dpsa='docker ps -a'
alias di='docker images'
alias dex='docker exec -it'
alias dlog='docker logs -f'
alias dcp='docker-compose'
alias dcup='docker-compose up -d'
alias dcdown='docker-compose down'
alias dclogs='docker-compose logs -f'

# Clean up
alias dprune='docker system prune -af --volumes'
alias dstop='docker stop $(docker ps -q)'
alias drm='docker rm $(docker ps -aq)'
```

## Quick Reference

| Task | Command |
|------|---------|
| Run container | `docker run -d nginx` |
| List containers | `docker ps` |
| Stop container | `docker stop <id>` |
| Remove container | `docker rm <id>` |
| Build image | `docker build -t myapp .` |
| List images | `docker images` |
| View logs | `docker logs <id>` |
| Shell access | `docker exec -it <id> bash` |
| Compose up | `docker-compose up -d` |
| Compose down | `docker-compose down` |
| Clean everything | `docker system prune -a` |

## Common Patterns

```bash
# Development with hot reload
docker run -d -p 3000:3000 -v $(pwd):/app node:16 npm run dev

# Database with persistent data
docker run -d -p 5432:5432 \
  -e POSTGRES_PASSWORD=secret \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:13

# Nginx reverse proxy
docker run -d -p 80:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
  nginx:alpine

# One-time command
docker run --rm -v $(pwd):/app node:16 npm install

# Background job with auto-remove
docker run -d --rm --name worker myapp:latest npm run worker
```

---

**Pro Tip:** Always use specific version tags in production!
```dockerfile
✅ FROM python:3.9.16-slim
❌ FROM python:latest
```

