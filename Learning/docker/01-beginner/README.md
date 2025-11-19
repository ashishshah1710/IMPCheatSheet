# 🐳 Docker Beginner Guide

## What is Docker?

Docker is a platform that enables developers to package applications and their dependencies into lightweight, portable containers. Think of containers as standardized units that contain everything needed to run your application.

### Why Docker?

**Before Docker:**
- "It works on my machine!" syndrome
- Complex environment setup
- Dependency conflicts
- Inconsistent deployments

**With Docker:**
- ✅ Consistent environments across development, testing, and production
- ✅ Fast and lightweight compared to VMs
- ✅ Easy application distribution
- ✅ Microservices architecture support

---

## 🏗️ Docker Architecture

```
┌─────────────────────────────────────────┐
│          Docker Client (CLI)            │
│         docker build, run, pull         │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│           Docker Daemon                 │
│    (Manages containers, images, etc)    │
└──────────────────┬──────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    ▼              ▼              ▼
┌─────────┐  ┌─────────┐  ┌─────────┐
│Container│  │Container│  │Container│
└─────────┘  └─────────┘  └─────────┘
```

### Key Components:
- **Docker Client:** Command-line tool to interact with Docker
- **Docker Daemon:** Background service that manages Docker objects
- **Docker Images:** Read-only templates to create containers
- **Docker Containers:** Runnable instances of images
- **Docker Registry:** Storage for Docker images (Docker Hub)

---

## 📦 Images vs Containers

### Docker Image
- Blueprint/Template for containers
- Read-only
- Contains application code, runtime, libraries, dependencies
- Stored in layers for efficiency

### Docker Container
- Running instance of an image
- Isolated process
- Has its own filesystem, network, process space
- Can be started, stopped, deleted

**Analogy:** Image is like a class, Container is like an object instance

---

## 🚀 Installation

### Windows/Mac
1. Download **Docker Desktop** from [docker.com](https://www.docker.com/products/docker-desktop)
2. Run the installer
3. Start Docker Desktop
4. Verify installation:

```bash
docker --version
docker run hello-world
```

### Linux
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group (avoid sudo)
sudo usermod -aG docker $USER
```

---

## 📝 Essential Docker Commands

### Working with Containers

```bash
# Run a container
docker run nginx

# Run in detached mode (background)
docker run -d nginx

# Run with a name
docker run -d --name my-nginx nginx

# Run with port mapping
docker run -d -p 8080:80 nginx

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop container_id

# Start a stopped container
docker start container_id

# Remove a container
docker rm container_id

# Remove a running container (force)
docker rm -f container_id

# View container logs
docker logs container_id

# Execute command in running container
docker exec -it container_id bash

# View container details
docker inspect container_id

# View container stats
docker stats
```

### Working with Images

```bash
# List local images
docker images

# Pull an image from Docker Hub
docker pull nginx

# Pull specific version
docker pull nginx:1.21

# Remove an image
docker rmi image_id

# Remove unused images
docker image prune

# Search for images
docker search nginx

# View image history
docker history image_name
```

### Cleanup Commands

```bash
# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune -a

# Remove all unused volumes
docker volume prune

# Remove everything unused
docker system prune -a

# View disk usage
docker system df
```

---

## 🎯 Hands-On Exercises

### Exercise 1: Run Your First Container

```bash
# Pull and run nginx web server
docker run -d -p 8080:80 --name my-web-server nginx

# Check it's running
docker ps

# Open browser to http://localhost:8080
# You should see "Welcome to nginx!"

# View logs
docker logs my-web-server

# Stop and remove
docker stop my-web-server
docker rm my-web-server
```

### Exercise 2: Interactive Containers

```bash
# Run Ubuntu container interactively
docker run -it ubuntu bash

# Inside the container, try:
cat /etc/os-release
ls /
apt update
apt install -y curl
curl https://example.com

# Exit the container
exit

# Run and auto-remove after exit
docker run -it --rm ubuntu bash
```

### Exercise 3: Container Inspection

```bash
# Run a container
docker run -d --name test-nginx nginx

# Inspect the container
docker inspect test-nginx

# View specific info (IP address)
docker inspect -f '{{.NetworkSettings.IPAddress}}' test-nginx

# View processes inside container
docker top test-nginx

# View resource usage
docker stats test-nginx

# Cleanup
docker rm -f test-nginx
```

### Exercise 4: Working with Different Images

```bash
# Python container
docker run -it python:3.9 python
>>> print("Hello from Docker!")
>>> exit()

# Node.js container
docker run -it node:16 node
> console.log("Node.js in Docker!");
> .exit

# Redis database
docker run -d --name my-redis redis

# Connect to Redis
docker exec -it my-redis redis-cli
127.0.0.1:6379> SET name "Docker"
127.0.0.1:6379> GET name
127.0.0.1:6379> exit

# Cleanup
docker rm -f my-redis
```

---

## 🎓 Practice Project: Simple Web Server

**Goal:** Run a static website using nginx

1. Create a directory for your project:
```bash
mkdir my-first-docker-app
cd my-first-docker-app
```

2. Create a simple HTML file:
```bash
# See index.html in the exercises folder
```

3. Run nginx and mount your HTML:
```bash
docker run -d -p 8080:80 -v ${PWD}:/usr/share/nginx/html --name my-site nginx
```

4. Visit http://localhost:8080

5. Modify index.html and refresh the browser

6. Cleanup:
```bash
docker rm -f my-site
```

---

## 🔍 Understanding Docker Run Options

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARGS]
```

Common options:
- `-d` : Detached mode (background)
- `-it` : Interactive with terminal
- `-p HOST:CONTAINER` : Port mapping
- `--name` : Assign a name
- `-v HOST:CONTAINER` : Volume mounting
- `-e` : Environment variables
- `--rm` : Auto-remove after exit
- `--network` : Connect to network
- `--memory` : Memory limit
- `--cpus` : CPU limit

---

## 📚 Docker Hub

Docker Hub is the default registry for Docker images.

### Finding Images
1. Visit [hub.docker.com](https://hub.docker.com)
2. Search for images (nginx, postgres, python, etc.)
3. Check:
   - Official images (verified)
   - Number of pulls
   - Last updated
   - Available tags

### Popular Official Images
- **nginx** - Web server
- **alpine** - Minimal Linux (5MB)
- **ubuntu** - Ubuntu OS
- **python** - Python runtime
- **node** - Node.js runtime
- **postgres** - PostgreSQL database
- **mysql** - MySQL database
- **redis** - Redis cache
- **mongo** - MongoDB database

---

## ⚠️ Common Beginner Mistakes

1. **Not stopping containers before removing**
   ```bash
   # Wrong
   docker rm container_id
   
   # Right
   docker stop container_id && docker rm container_id
   # Or use force
   docker rm -f container_id
   ```

2. **Forgetting port mapping**
   ```bash
   # Won't be accessible
   docker run nginx
   
   # Accessible on localhost:8080
   docker run -p 8080:80 nginx
   ```

3. **Not naming containers**
   ```bash
   # Hard to manage
   docker run -d nginx
   
   # Easy to reference
   docker run -d --name my-nginx nginx
   ```

4. **Not cleaning up**
   ```bash
   # Regularly clean up unused resources
   docker system prune
   ```

---

## ✅ Beginner Checklist

- [ ] Docker installed and running
- [ ] Understand images vs containers
- [ ] Can run, stop, and remove containers
- [ ] Understand port mapping
- [ ] Can view logs and inspect containers
- [ ] Know how to search Docker Hub
- [ ] Comfortable with basic docker commands
- [ ] Completed all exercises

---

## 🎯 Next Steps

Once you've mastered the basics:
1. Complete all exercises
2. Experiment with different images
3. Practice the commands daily
4. Move to: `docker/02-intermediate/`

**Next Topic:** Creating your own Docker images with Dockerfiles! 🚀

