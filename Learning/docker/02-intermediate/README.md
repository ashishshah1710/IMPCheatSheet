# 🐳 Docker Intermediate Guide

## Building Custom Images with Dockerfile

Now that you understand how to use existing Docker images, it's time to create your own!

### What is a Dockerfile?

A Dockerfile is a text file containing instructions to build a Docker image. It's like a recipe for creating your custom image.

---

## 📝 Dockerfile Basics

### Basic Structure

```dockerfile
# Start with a base image
FROM ubuntu:20.04

# Set metadata
LABEL maintainer="your-email@example.com"

# Run commands
RUN apt-get update && apt-get install -y python3

# Copy files
COPY app.py /app/

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 8000

# Command to run
CMD ["python3", "app.py"]
```

### Common Dockerfile Instructions

| Instruction | Purpose | Example |
|------------|---------|---------|
| `FROM` | Base image | `FROM python:3.9` |
| `RUN` | Execute command during build | `RUN pip install flask` |
| `COPY` | Copy files from host to image | `COPY . /app` |
| `ADD` | Copy + extract archives | `ADD app.tar.gz /app` |
| `WORKDIR` | Set working directory | `WORKDIR /app` |
| `ENV` | Set environment variable | `ENV NODE_ENV=production` |
| `EXPOSE` | Document port | `EXPOSE 3000` |
| `CMD` | Default command (can be overridden) | `CMD ["npm", "start"]` |
| `ENTRYPOINT` | Main command (not overridden) | `ENTRYPOINT ["python"]` |
| `VOLUME` | Create mount point | `VOLUME /data` |
| `USER` | Set user | `USER appuser` |
| `ARG` | Build-time variable | `ARG VERSION=1.0` |

---

## 🏗️ Building Images

### Build Command

```bash
# Basic build
docker build -t my-app:latest .

# Build with specific Dockerfile
docker build -t my-app:v1 -f Dockerfile.dev .

# Build with build arguments
docker build --build-arg VERSION=2.0 -t my-app:2.0 .

# Build without cache
docker build --no-cache -t my-app:latest .
```

### Best Practices

1. **Use specific base image versions**
```dockerfile
# Bad - version changes unexpectedly
FROM python

# Good - predictable builds
FROM python:3.9-slim
```

2. **Minimize layers**
```dockerfile
# Bad - creates 3 layers
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip

# Good - creates 1 layer
RUN apt-get update && \
    apt-get install -y python3 pip && \
    rm -rf /var/lib/apt/lists/*
```

3. **Order matters for caching**
```dockerfile
# Good - dependencies change less often
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Bad - invalidates cache on any code change
COPY . .
RUN pip install -r requirements.txt
```

4. **Use .dockerignore**
```
node_modules
*.log
.git
.env
__pycache__
*.pyc
```

---

## 🎯 Hands-On: Python Web App

### Step 1: Create Application Files

**app.py**
```python
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Dockerized Flask!',
        'environment': os.getenv('ENV', 'development')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**requirements.txt**
```
flask==2.3.0
```

### Step 2: Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port
EXPOSE 5000

# Set environment variable
ENV ENV=production

# Run the application
CMD ["python", "app.py"]
```

### Step 3: Build and Run

```bash
# Build the image
docker build -t flask-app:1.0 .

# Run the container
docker run -d -p 5000:5000 --name my-flask-app flask-app:1.0

# Test it
curl http://localhost:5000
curl http://localhost:5000/health

# Check logs
docker logs my-flask-app

# Cleanup
docker rm -f my-flask-app
```

---

## 🔧 Docker Compose

Docker Compose is a tool for defining and running multi-container applications.

### Why Docker Compose?

- Define multi-container apps in a single file
- Start everything with one command
- Manage dependencies between services
- Easy environment configuration

### docker-compose.yml Structure

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - ENV=production
    volumes:
      - ./app:/app
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

### Docker Compose Commands

```bash
# Start all services
docker-compose up

# Start in detached mode
docker-compose up -d

# Build and start
docker-compose up --build

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# View logs
docker-compose logs

# Follow logs for specific service
docker-compose logs -f web

# List running services
docker-compose ps

# Execute command in service
docker-compose exec web bash

# Scale a service
docker-compose up -d --scale web=3

# Restart a service
docker-compose restart web
```

---

## 🎯 Project: Full Stack Application

Let's build a complete app with frontend, backend, and database!

### Project Structure
```
my-app/
├── docker-compose.yml
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   └── style.css
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── .env
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
  
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/myapp
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres-data:
```

### Frontend Dockerfile

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/

EXPOSE 80
```

### Backend Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Running the Project

```bash
# Start everything
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Stop everything
docker-compose down
```

---

## 🌐 Docker Networking

### Network Types

1. **Bridge (default)** - Containers on same host
2. **Host** - Use host's network directly
3. **None** - No network
4. **Overlay** - Multi-host networking

### Network Commands

```bash
# List networks
docker network ls

# Create network
docker network create my-network

# Run container on network
docker run -d --name app1 --network my-network nginx

# Inspect network
docker network inspect my-network

# Connect container to network
docker network connect my-network app2

# Disconnect
docker network disconnect my-network app2

# Remove network
docker network rm my-network
```

### Container Communication

```bash
# Create network
docker network create app-network

# Run database
docker run -d --name db --network app-network postgres

# Run app (can access db by name)
docker run -d --name web --network app-network my-app

# Inside app container: postgresql://db:5432
```

---

## 💾 Docker Volumes

### Types of Storage

1. **Volumes** - Managed by Docker (recommended)
2. **Bind Mounts** - Direct host path mapping
3. **tmpfs** - Temporary in-memory storage

### Volume Commands

```bash
# Create volume
docker volume create my-data

# List volumes
docker volume ls

# Inspect volume
docker volume inspect my-data

# Use volume
docker run -d -v my-data:/data nginx

# Remove volume
docker volume rm my-data

# Remove all unused volumes
docker volume prune
```

### Volume vs Bind Mount

```bash
# Volume (managed by Docker)
docker run -v my-volume:/data nginx

# Bind mount (specific host path)
docker run -v /host/path:/container/path nginx
docker run -v ${PWD}:/app nginx
```

### Data Persistence Example

```bash
# Run MySQL with persistent data
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  -v mysql-data:/var/lib/mysql \
  mysql:8

# Create database and data
docker exec -it mysql mysql -psecret
CREATE DATABASE testdb;
USE testdb;
CREATE TABLE users (id INT, name VARCHAR(50));
INSERT INTO users VALUES (1, 'John');

# Remove container
docker rm -f mysql

# Run new container with same volume
docker run -d \
  --name mysql2 \
  -e MYSQL_ROOT_PASSWORD=secret \
  -v mysql-data:/var/lib/mysql \
  mysql:8

# Data still exists!
docker exec -it mysql2 mysql -psecret -e "SELECT * FROM testdb.users"
```

---

## 🛡️ Docker Security Basics

### Best Practices

1. **Don't run as root**
```dockerfile
FROM python:3.9-slim

RUN useradd -m appuser
USER appuser

WORKDIR /home/appuser/app
COPY --chown=appuser:appuser . .
```

2. **Use official images**
```dockerfile
# Use official, minimal images
FROM python:3.9-slim
# Not random images from unknown sources
```

3. **Scan images for vulnerabilities**
```bash
docker scan my-image:latest
```

4. **Don't store secrets in images**
```bash
# Use environment variables
docker run -e DB_PASSWORD=secret my-app

# Or Docker secrets (Swarm)
echo "secret123" | docker secret create db_password -
```

5. **Limit resources**
```bash
docker run --memory="512m" --cpus="1" my-app
```

---

## ✅ Intermediate Checklist

- [ ] Can write Dockerfiles
- [ ] Understand image layers and caching
- [ ] Built custom images successfully
- [ ] Created .dockerignore files
- [ ] Understand Docker Compose
- [ ] Can create multi-container apps
- [ ] Understand Docker networking
- [ ] Know how to persist data with volumes
- [ ] Aware of basic security practices

---

## 🎯 Practice Exercises

### Exercise 1: Build Node.js App
Create a Dockerfile for a Node.js application with package.json

### Exercise 2: Multi-Stage Build
Build an optimized image using multi-stage builds

### Exercise 3: WordPress with Docker Compose
Deploy WordPress with MySQL using docker-compose

### Exercise 4: Custom Network
Create two containers that communicate on a custom network

---

## 🚀 Next Steps

You're ready for advanced Docker concepts!

Move to: `docker/03-advanced/`

**Next Topics:**
- Multi-stage builds
- Image optimization
- Docker in production
- CI/CD pipelines

