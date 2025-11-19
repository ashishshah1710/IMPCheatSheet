# 🚀 Get Started in 5 Minutes

The fastest way to begin your Docker, Kubernetes, and AWS journey!

---

## ✅ Quick Setup Checklist

Before you start learning, set up your environment:

### 1. Install Docker Desktop (5 minutes)

**Windows/Mac:**
1. Download: [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Run installer
3. Start Docker Desktop
4. Wait for "Docker Desktop is running"

**Verify:**
```bash
docker --version
# Should output: Docker version 24.x.x
```

**Test:**
```bash
docker run hello-world
# Should see: "Hello from Docker!"
```

---

### 2. Enable Kubernetes (2 minutes)

**Docker Desktop:**
1. Open Docker Desktop
2. Settings → Kubernetes
3. ✅ Enable Kubernetes
4. Click "Apply & Restart"
5. Wait for green indicator

**Verify:**
```bash
kubectl version --client
# Should output: Client Version: v1.28.x
```

**Test:**
```bash
kubectl get nodes
# Should show one node (docker-desktop)
```

---

### 3. Install AWS CLI (3 minutes)

**Windows:**
```bash
# Using Chocolatey
choco install awscli

# Or download MSI installer
# https://aws.amazon.com/cli/
```

**Mac:**
```bash
brew install awscli
```

**Linux:**
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**Verify:**
```bash
aws --version
# Should output: aws-cli/2.x.x
```

---

### 4. Create AWS Account (10 minutes)

1. Go to [aws.amazon.com](https://aws.amazon.com)
2. Click "Create an AWS Account"
3. Follow the registration process
4. **Set up billing alerts immediately!**

---

## 🎯 Your First 30 Minutes

### Minute 1-10: Docker Basics

```bash
# 1. Run a web server
docker run -d -p 8080:80 --name my-web nginx

# 2. Check it's running
docker ps

# 3. View in browser
# Open: http://localhost:8080

# 4. View logs
docker logs my-web

# 5. Stop and remove
docker stop my-web
docker rm my-web
```

✅ **You just deployed a web server in a container!**

---

### Minute 11-20: Build Your First Image

```bash
# 1. Create a directory
mkdir my-first-docker-app
cd my-first-docker-app

# 2. Create a simple HTML file
cat > index.html << EOF
<!DOCTYPE html>
<html>
<head><title>My Docker App</title></head>
<body>
  <h1>Hello from my Docker container! 🐳</h1>
  <p>I built this!</p>
</body>
</html>
EOF

# 3. Create Dockerfile
cat > Dockerfile << EOF
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EOF

# 4. Build image
docker build -t my-first-app .

# 5. Run your app
docker run -d -p 8080:80 my-first-app

# 6. View in browser
# Open: http://localhost:8080

# 7. Clean up
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
```

✅ **You just created and deployed your own Docker image!**

---

### Minute 21-30: Kubernetes Basics

```bash
# 1. Create a deployment
kubectl create deployment hello --image=nginx

# 2. Check it's running
kubectl get deployments
kubectl get pods

# 3. Expose it as a service
kubectl expose deployment hello --port=80 --type=NodePort

# 4. Get the service
kubectl get services

# 5. Access the application
# Windows/Mac: Open browser to http://localhost:<NodePort>
# Or use port forwarding:
kubectl port-forward service/hello 8080:80

# 6. Scale it up
kubectl scale deployment hello --replicas=3

# 7. Check pods again
kubectl get pods
# You should see 3 pods now!

# 8. Clean up
kubectl delete deployment hello
kubectl delete service hello
```

✅ **You just deployed and scaled an application on Kubernetes!**

---

## 📚 What to Learn Next

### Day 1: Docker Deep Dive (2 hours)

**Read:**
- `docker/01-beginner/README.md`

**Practice:**
- Run different containers
- Learn Docker commands
- Mount volumes
- Use port mapping

**Goal:** Understand container basics

---

### Day 2: Dockerfiles (2 hours)

**Read:**
- `docker/02-intermediate/README.md` (Dockerfile section)

**Practice:**
- Write Dockerfiles
- Build custom images
- Use .dockerignore
- Optimize images

**Goal:** Build custom Docker images

---

### Day 3: Docker Compose (2 hours)

**Read:**
- `docker/02-intermediate/README.md` (Docker Compose section)

**Practice:**
- Create docker-compose.yml
- Run multi-container apps
- Use networks and volumes

**Goal:** Orchestrate multiple containers

---

### Day 4: Kubernetes Basics (2 hours)

**Read:**
- `kubernetes/01-beginner/README.md`

**Practice:**
- kubectl commands
- Create pods
- Create deployments
- Expose services

**Goal:** Deploy apps to K8s

---

### Day 5: Kubernetes Manifests (2 hours)

**Read:**
- Kubernetes YAML section

**Practice:**
- Write YAML files
- Apply manifests
- Update deployments
- Scale applications

**Goal:** Use declarative configuration

---

### Day 6-7: First Project (4-6 hours)

**Build:**
- `projects/01-containerized-blog/`

**Learn:**
- Full stack deployment
- Docker Compose
- Database persistence
- Container networking

**Goal:** Complete end-to-end application

---

## 🎯 Learning Path Decision

Choose your path based on your goals:

### Path A: I Want a DevOps Job

**Timeline:** 12 weeks  
**Focus:** Docker → Kubernetes → AWS → Projects  
**Follow:** `STUDY-PLAN.md` (Standard Plan)  
**Goal:** Build portfolio + Get certified

---

### Path B: I'm a Developer

**Timeline:** 8 weeks  
**Focus:** Docker → Kubernetes → CI/CD  
**Skip:** Advanced AWS (focus on ECS/EKS)  
**Goal:** Containerize and deploy applications

---

### Path C: I'm a Cloud Engineer

**Timeline:** 10 weeks  
**Focus:** AWS → Docker → ECS/EKS  
**Emphasize:** Infrastructure as Code  
**Goal:** Cloud-native architectures

---

## 📖 Essential Resources

### Must-Read Documents

1. **`README.md`** - Overview and learning paths
2. **`QUICKSTART.md`** - Quick guides and examples
3. **`STUDY-PLAN.md`** - Detailed 12-week plan
4. **`TROUBLESHOOTING.md`** - When things don't work

### Cheat Sheets

1. **`docker/CHEATSHEET.md`** - All Docker commands
2. **`kubernetes/CHEATSHEET.md`** - All kubectl commands
3. **`aws/CHEATSHEET.md`** - All AWS CLI commands

### Learning Materials

1. **`docker/01-beginner/`** - Start here for Docker
2. **`kubernetes/01-beginner/`** - Start here for K8s
3. **`aws/01-beginner/`** - Start here for AWS

---

## 🎓 Certification Roadmap

### 3 Months: CKA (Certified Kubernetes Administrator)
- **Cost:** $395
- **Best for:** Kubernetes focus
- **Prep time:** 3-4 months

### 3 Months: AWS Solutions Architect Associate
- **Cost:** $150
- **Best for:** Cloud focus
- **Prep time:** 2-3 months

### 6 Months: Both Certifications
- **Order:** Learn fundamentals → Pick one → Get certified → Learn other → Get certified
- **Total cost:** $545
- **Career impact:** High

---

## 💰 Cost Considerations

### Free Resources
- ✅ Docker (runs locally)
- ✅ Kubernetes (runs locally)
- ✅ AWS Free Tier (12 months)
- ✅ All learning materials in this repo

### Potential Costs
- AWS usage beyond free tier
- Certification exams
- Premium courses (optional)

### Staying Within Free Tier
1. **Set up billing alerts**
2. **Stop resources when not using**
3. **Use t2.micro instances only**
4. **Delete resources after practice**
5. **Monitor costs daily**

---

## 🎯 30-Day Challenge

Can you do it in 30 days? Yes, if you commit 3-4 hours daily!

### Week 1: Docker
- Days 1-3: Basics
- Days 4-5: Dockerfiles
- Days 6-7: Docker Compose + Project

### Week 2: Kubernetes
- Days 8-10: K8s Basics
- Days 11-12: Deployments & Services
- Days 13-14: ConfigMaps + Project

### Week 3: AWS
- Days 15-17: AWS Basics + IAM
- Days 18-19: EC2 + S3
- Days 20-21: RDS + Project

### Week 4: Integration
- Days 22-24: ECS/EKS
- Days 25-27: CI/CD
- Days 28-30: Final Project

---

## ✅ Daily Routine

### Morning (1 hour)
- Read theory
- Watch tutorials
- Take notes

### Evening (1-2 hours)
- Hands-on practice
- Build projects
- Solve problems

### Weekend (4-6 hours)
- Major projects
- Review concepts
- Portfolio work

---

## 🆘 When You're Stuck

1. **Check logs first**
```bash
docker logs <container>
kubectl logs <pod>
```

2. **Google the error**
   - Copy exact error message
   - Add "docker" or "kubernetes" to search

3. **Check troubleshooting guide**
   - Read: `TROUBLESHOOTING.md`

4. **Ask for help**
   - Stack Overflow
   - Reddit (r/docker, r/kubernetes, r/aws)
   - Discord/Slack communities

---

## 🎉 You're Ready!

You now have:
- ✅ Environment set up
- ✅ First containers running
- ✅ Basic commands learned
- ✅ Clear learning path
- ✅ Resources available

### Next Steps:

1. **Choose your learning path**
   - Read `STUDY-PLAN.md`

2. **Start with Docker**
   - Read `docker/01-beginner/README.md`
   - Complete all exercises

3. **Build projects**
   - See `projects/README.md`

4. **Join communities**
   - Get help when stuck
   - Share your progress

5. **Stay consistent**
   - Study every day
   - Track your progress
   - Celebrate milestones

---

## 📈 Track Your Progress

```markdown
## My Learning Journey

**Started:** [Date]
**Goal:** [Your goal]
**Daily commitment:** [Hours]

### Week 1
- [ ] Docker basics
- [ ] First Dockerfile
- [ ] Docker Compose
- [ ] Project 1

### Week 2
- [ ] Kubernetes basics
- [ ] Deployments
- [ ] Services
- [ ] Project 2

### Week 3
- [ ] AWS account
- [ ] EC2 & S3
- [ ] RDS
- [ ] Project 3

### Completed Projects
1. [ ] Blog application
2. [ ] Microservices
3. [ ] AWS deployment
4. [ ] Full DevOps pipeline
```

---

## 🌟 Success Stories

**What you'll be able to do after 12 weeks:**

- ✅ Containerize any application
- ✅ Deploy to Kubernetes
- ✅ Build infrastructure on AWS
- ✅ Create CI/CD pipelines
- ✅ Monitor production systems
- ✅ Troubleshoot issues
- ✅ Pass certification exams
- ✅ Get DevOps jobs

---

## 💪 Motivation

> "The expert in anything was once a beginner."

Every DevOps engineer started exactly where you are now. The technologies might seem complex, but with consistent practice, you'll master them.

**Remember:**
- Progress over perfection
- Practice over theory
- Projects over tutorials
- Consistency over intensity

---

## 🚀 Let's Begin!

**Your journey starts NOW!**

1. Open `docker/01-beginner/README.md`
2. Run your first command
3. Build something
4. Never stop learning

---

**Welcome to the world of DevOps! 🎉**

You've got this! 💪

