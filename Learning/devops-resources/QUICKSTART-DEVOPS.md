# 🚀 Quick Start Guide

Get started with Docker, Kubernetes, and AWS in just a few hours!

---

## ⏱️ 1-Hour Quick Start

If you only have one hour, start here to get the fundamentals:

### Docker (20 minutes)

```bash
# 1. Install Docker Desktop
# Download from: https://www.docker.com/products/docker-desktop

# 2. Verify installation
docker --version

# 3. Run your first container
docker run hello-world

# 4. Run a web server
docker run -d -p 8080:80 nginx

# 5. Check it's running
# Open browser: http://localhost:8080

# 6. View running containers
docker ps

# 7. Stop the container
docker stop <container-id>

# 8. Clean up
docker rm <container-id>
```

**✅ You now understand containers!**

### Kubernetes (20 minutes)

```bash
# 1. Enable Kubernetes in Docker Desktop
# Settings → Kubernetes → Enable Kubernetes

# 2. Verify installation
kubectl version --client

# 3. Create a deployment
kubectl create deployment nginx --image=nginx

# 4. View the deployment
kubectl get deployments
kubectl get pods

# 5. Expose the deployment
kubectl expose deployment nginx --port=80 --type=NodePort

# 6. Get the service URL
kubectl get services

# 7. Access the application
# Open browser: http://localhost:<NodePort>

# 8. Clean up
kubectl delete deployment nginx
kubectl delete service nginx
```

**✅ You now understand Kubernetes basics!**

### AWS (20 minutes)

```bash
# 1. Create AWS Account
# Visit: https://aws.amazon.com

# 2. Install AWS CLI
# Windows: choco install awscli
# Mac: brew install awscli
# Linux: apt install awscli

# 3. Configure AWS CLI
aws configure
# Enter your Access Key, Secret Key, Region (us-east-1), Output format (json)

# 4. Verify configuration
aws sts get-caller-identity

# 5. Create an S3 bucket
aws s3 mb s3://my-first-bucket-$(date +%s)

# 6. Upload a file
echo "Hello AWS!" > hello.txt
aws s3 cp hello.txt s3://my-first-bucket-XXXXXX/

# 7. List files in bucket
aws s3 ls s3://my-first-bucket-XXXXXX/

# 8. Download file
aws s3 cp s3://my-first-bucket-XXXXXX/hello.txt ./hello-downloaded.txt

# 9. Clean up
aws s3 rb s3://my-first-bucket-XXXXXX --force
```

**✅ You now understand AWS basics!**

---

## 📅 3-Day Quick Start

### Day 1: Docker Essentials

**Morning (2 hours):** Docker Fundamentals
- Read: `docker/01-beginner/README.md`
- Practice all commands in the beginner guide
- Complete Exercise 1-4

**Afternoon (2 hours):** Building Images
- Read: `docker/02-intermediate/README.md` (Dockerfile section)
- Create your first Dockerfile
- Build and run custom images

**Evening (1 hour):** Docker Compose
- Learn Docker Compose basics
- Run a multi-container application
- Deploy the Flask + Postgres example

**🎯 Day 1 Goal:** Deploy a web app with database using Docker Compose

---

### Day 2: Kubernetes Essentials

**Morning (2 hours):** Kubernetes Basics
- Read: `kubernetes/01-beginner/README.md`
- Install Minikube or use Docker Desktop Kubernetes
- Practice kubectl commands

**Afternoon (2 hours):** Deployments and Services
- Create your first deployment
- Expose services
- Scale applications
- Perform rolling updates

**Evening (1 hour):** Hands-On Project
- Deploy a complete web application
- Use ConfigMaps for configuration
- Set up proper health checks

**🎯 Day 2 Goal:** Deploy and scale a containerized application on Kubernetes

---

### Day 3: AWS Essentials

**Morning (2 hours):** AWS Fundamentals
- Read: `aws/01-beginner/README.md`
- Set up IAM user
- Launch first EC2 instance
- Create S3 bucket

**Afternoon (2 hours):** Practical AWS
- Deploy web server on EC2
- Set up RDS database
- Configure VPC and Security Groups

**Evening (1 hour):** Integration
- Deploy Docker container on EC2
- Use ECR for container images
- Basic monitoring with CloudWatch

**🎯 Day 3 Goal:** Deploy a web application on AWS with database

---

## 🎯 First Projects

### Project 1: Containerized Web App (Docker)

**Time:** 1 hour  
**Difficulty:** Beginner

Create a simple Node.js or Python web app and containerize it.

```dockerfile
# Dockerfile
FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

```bash
# Build and run
docker build -t my-web-app .
docker run -p 3000:3000 my-web-app
```

### Project 2: Microservices with Docker Compose

**Time:** 2 hours  
**Difficulty:** Intermediate

Build a system with:
- Frontend (React/Vue)
- Backend API (Node.js/Python)
- Database (PostgreSQL/MongoDB)
- Redis Cache

```yaml
# docker-compose.yml
version: '3.8'
services:
  frontend:
    build: ./frontend
    ports:
      - "80:80"
  backend:
    build: ./backend
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=db
      - REDIS_HOST=redis
  db:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=secret
  redis:
    image: redis:alpine
```

### Project 3: Deploy to Kubernetes

**Time:** 2 hours  
**Difficulty:** Intermediate

Take your containerized app and deploy to Kubernetes:

1. Create Deployment YAML
2. Create Service YAML
3. Add ConfigMap for configuration
4. Set up health checks
5. Scale to 3 replicas

### Project 4: Production AWS Deployment

**Time:** 4 hours  
**Difficulty:** Advanced

Deploy a complete production-ready application:

**Architecture:**
```
Internet → ALB → EC2 Auto Scaling → RDS → S3
           ↓
      CloudWatch (Monitoring)
```

**Components:**
- VPC with public and private subnets
- Application Load Balancer
- EC2 Auto Scaling Group
- RDS database (Multi-AZ)
- S3 for static assets
- CloudWatch for monitoring

---

## 📖 Learning Paths

### Path A: Developer Focus

**Goal:** Build and deploy applications

1. **Week 1:** Docker
   - Containerize applications
   - Multi-stage builds
   - Docker Compose

2. **Week 2:** Kubernetes
   - Deploy to K8s
   - Services and Ingress
   - ConfigMaps and Secrets

3. **Week 3:** AWS
   - ECS/EKS
   - ECR
   - CI/CD with CodePipeline

### Path B: DevOps Focus

**Goal:** Infrastructure and automation

1. **Week 1:** Docker + Kubernetes
   - Container fundamentals
   - Orchestration basics
   - Helm charts

2. **Week 2:** AWS Infrastructure
   - VPC design
   - EC2 and Auto Scaling
   - Load Balancers
   - RDS

3. **Week 3:** IaC and Automation
   - Terraform/CloudFormation
   - CI/CD pipelines
   - Monitoring and logging

### Path C: Cloud Architect Focus

**Goal:** Design scalable systems

1. **Week 1:** Fundamentals
   - Docker basics
   - Kubernetes architecture
   - AWS services overview

2. **Week 2:** Architecture Patterns
   - Microservices
   - Serverless
   - High availability
   - Disaster recovery

3. **Week 3:** Production Systems
   - EKS production deployment
   - Security best practices
   - Cost optimization
   - Monitoring and observability

---

## 🎓 Certification Paths

### Docker Certified Associate (DCA)

**Prerequisites:** 6 months Docker experience

**Exam Topics:**
- Image creation and management
- Container orchestration
- Storage and volumes
- Networking
- Security

**Study Time:** 2-3 months  
**Cost:** $195

### Certified Kubernetes Administrator (CKA)

**Prerequisites:** Basic K8s knowledge

**Exam Topics:**
- Cluster architecture
- Workloads and scheduling
- Services and networking
- Storage
- Troubleshooting

**Study Time:** 3-4 months  
**Cost:** $395

### AWS Certified Solutions Architect - Associate

**Prerequisites:** 1 year AWS experience

**Exam Topics:**
- Resilient architectures
- High-performing architectures
- Secure applications
- Cost-optimized architectures

**Study Time:** 2-3 months  
**Cost:** $150

---

## 💡 Tips for Success

### 1. Practice Daily

Set aside 1-2 hours every day for hands-on practice.

```bash
# Create a daily practice routine
# Monday: Docker containers
# Tuesday: Dockerfile creation
# Wednesday: Kubernetes pods
# Thursday: Kubernetes services
# Friday: AWS services
# Weekend: Projects
```

### 2. Build Real Projects

Don't just follow tutorials. Build something real:
- Personal website
- Blog platform
- API service
- Data pipeline
- Monitoring dashboard

### 3. Use the Free Tiers

**Docker/Kubernetes:**
- Run locally (100% free)
- Docker Desktop (free for personal use)
- Minikube/Kind (free)

**AWS Free Tier:**
- EC2: 750 hours/month (t2.micro)
- S3: 5GB storage
- RDS: 750 hours/month (db.t2.micro)
- Lambda: 1M requests/month

⚠️ **Set up billing alerts!**

### 4. Join Communities

- [Docker Community Slack](https://dockercommunity.slack.com)
- [Kubernetes Slack](https://slack.k8s.io)
- [AWS Reddit](https://reddit.com/r/aws)
- Stack Overflow
- Dev.to

### 5. Document Your Learning

Keep a learning journal:
```markdown
# Date: 2024-01-15

## What I Learned
- Docker multi-stage builds
- How to optimize image size

## What I Built
- Optimized Node.js image from 800MB to 150MB

## Challenges
- Understanding layer caching

## Next Steps
- Learn Docker Compose
- Build multi-container app
```

---

## 🔧 Essential Tools

### Code Editor
- **VS Code** (recommended)
  - Docker extension
  - Kubernetes extension
  - AWS Toolkit

### Terminal Tools
- **kubectl** - Kubernetes CLI
- **aws-cli** - AWS CLI
- **docker** - Docker CLI
- **k9s** - Kubernetes TUI
- **lens** - Kubernetes IDE

### Monitoring
- **ctop** - Container monitoring
- **lazydocker** - Docker TUI
- **AWS CloudWatch**

---

## 📚 Recommended Resources

### Books
- "Docker Deep Dive" by Nigel Poulton
- "Kubernetes Up and Running" by Kelsey Hightower
- "AWS Certified Solutions Architect Study Guide"

### Online Courses
- Docker Mastery (Udemy)
- Kubernetes for Developers (Udemy)
- AWS Solutions Architect (A Cloud Guru)

### Practice Platforms
- [KillerCoda](https://killercoda.com) - Interactive scenarios
- [Play with Docker](https://labs.play-with-docker.com)
- [Play with Kubernetes](https://labs.play-with-k8s.com)

### YouTube Channels
- TechWorld with Nana
- That DevOps Guy
- Fireship
- freeCodeCamp

---

## ✅ 30-Day Challenge

| Week | Focus | Daily Task |
|------|-------|------------|
| 1 | Docker | Run, build, and deploy containers |
| 2 | Kubernetes | Deploy and scale applications |
| 3 | AWS | Launch EC2, S3, RDS services |
| 4 | Integration | Build end-to-end project |

**Daily Commitment:** 1-2 hours  
**Weekend:** 4-6 hours on projects

---

## 🎯 Next Steps

1. ✅ Complete the 1-hour quick start above
2. ✅ Choose your learning path (Developer/DevOps/Architect)
3. ✅ Set up your development environment
4. ✅ Start with Docker beginner guide
5. ✅ Build your first project
6. ✅ Join the communities
7. ✅ Keep learning and building!

---

**Remember:** The best way to learn is by doing. Don't just read—practice, build, break things, and learn from your mistakes!

Good luck on your learning journey! 🚀

