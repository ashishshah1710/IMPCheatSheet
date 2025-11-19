# 🎯 Hands-On Projects

Apply your Docker, Kubernetes, and AWS knowledge with these practical projects!

---

## Project Difficulty Levels

- 🟢 **Beginner:** Basic concepts, 1-2 hours
- 🟡 **Intermediate:** Multiple technologies, 3-5 hours
- 🔴 **Advanced:** Production-ready, 6+ hours

---

## 🟢 Project 1: Containerized Blog Application

**Technologies:** Docker, Docker Compose  
**Time:** 2 hours  
**Difficulty:** Beginner

### Goal
Build a simple blog application with frontend, backend, and database.

### Architecture
```
┌──────────────┐
│   Frontend   │ (React/HTML)
│   Port 3000  │
└──────┬───────┘
       │
┌──────▼───────┐
│   Backend    │ (Node.js/Python)
│   Port 5000  │
└──────┬───────┘
       │
┌──────▼───────┐
│   Database   │ (PostgreSQL)
│   Port 5432  │
└──────────────┘
```

### Steps

1. **Create project structure**
```bash
mkdir blog-app
cd blog-app
mkdir frontend backend
```

2. **Backend (Node.js + Express)**
```javascript
// backend/server.js
const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const pool = new Pool({
  host: process.env.DB_HOST || 'db',
  database: 'blog',
  user: 'postgres',
  password: 'secret',
  port: 5432,
});

app.get('/api/posts', async (req, res) => {
  const { rows } = await pool.query('SELECT * FROM posts ORDER BY created_at DESC');
  res.json(rows);
});

app.post('/api/posts', async (req, res) => {
  const { title, content } = req.body;
  const { rows } = await pool.query(
    'INSERT INTO posts (title, content) VALUES ($1, $2) RETURNING *',
    [title, content]
  );
  res.json(rows[0]);
});

app.listen(5000, () => console.log('Server running on port 5000'));
```

3. **Backend Dockerfile**
```dockerfile
# backend/Dockerfile
FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5000
CMD ["node", "server.js"]
```

4. **Frontend (React)**
```javascript
// frontend/src/App.js
import React, { useState, useEffect } from 'react';

function App() {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    const response = await fetch('http://localhost:5000/api/posts');
    const data = await response.json();
    setPosts(data);
  };

  const createPost = async (e) => {
    e.preventDefault();
    await fetch('http://localhost:5000/api/posts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, content }),
    });
    setTitle('');
    setContent('');
    fetchPosts();
  };

  return (
    <div className="App">
      <h1>My Blog</h1>
      <form onSubmit={createPost}>
        <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" />
        <textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder="Content" />
        <button type="submit">Create Post</button>
      </form>
      <div>
        {posts.map((post) => (
          <div key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

5. **Docker Compose**
```yaml
# docker-compose.yml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - REACT_APP_API_URL=http://localhost:5000

  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=db
      - DB_USER=postgres
      - DB_PASSWORD=secret
      - DB_NAME=blog
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=blog
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  postgres-data:
```

6. **Database initialization**
```sql
-- init.sql
CREATE TABLE IF NOT EXISTS posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO posts (title, content) VALUES
  ('First Post', 'Welcome to my blog!'),
  ('Docker is awesome', 'Containerization makes deployment easy!');
```

7. **Run the application**
```bash
docker-compose up --build
```

### Success Criteria
- ✅ All containers running
- ✅ Frontend accessible at http://localhost:3000
- ✅ Can create new posts
- ✅ Posts persist after restart

---

## 🟡 Project 2: Kubernetes Microservices

**Technologies:** Docker, Kubernetes  
**Time:** 4 hours  
**Difficulty:** Intermediate

### Goal
Deploy a microservices architecture on Kubernetes with service discovery and scaling.

### Architecture
```
           ┌──────────────┐
           │   Ingress    │
           └──────┬───────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
    ┌────────┐        ┌────────┐
    │Frontend│        │   API  │
    │Service │        │Gateway │
    └────────┘        └───┬────┘
                          │
                 ┌────────┼────────┐
                 ▼        ▼        ▼
            ┌────────┐ ┌────────┐ ┌────────┐
            │ Users  │ │Products│ │ Orders │
            │Service │ │Service │ │Service │
            └────┬───┘ └────┬───┘ └────┬───┘
                 │          │          │
                 └──────────┼──────────┘
                            ▼
                       ┌─────────┐
                       │Database │
                       └─────────┘
```

### Files Provided
See `projects/02-kubernetes-microservices/` directory for complete code.

### Key Concepts
- Multiple microservices
- Service-to-service communication
- ConfigMaps for configuration
- Secrets for sensitive data
- Horizontal Pod Autoscaling
- Liveness and Readiness probes

### Deployment
```bash
cd projects/02-kubernetes-microservices/

# Create namespace
kubectl create namespace microservices

# Apply all configurations
kubectl apply -f k8s/ -n microservices

# Check status
kubectl get all -n microservices

# Scale services
kubectl scale deployment users-api --replicas=3 -n microservices

# View logs
kubectl logs -f deployment/users-api -n microservices
```

---

## 🟡 Project 3: AWS Full Stack Deployment

**Technologies:** Docker, AWS (EC2, RDS, S3, ALB)  
**Time:** 5 hours  
**Difficulty:** Intermediate

### Goal
Deploy a production-ready web application on AWS.

### Architecture
```
Internet
    │
    ▼
┌─────────────────┐
│ Route 53 (DNS)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ CloudFront CDN  │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌──────┐  ┌──────┐
│  ALB │  │  S3  │ (Static Assets)
└──┬───┘  └──────┘
   │
   ├─────────────┐
   ▼             ▼
┌─────┐      ┌─────┐
│ EC2 │      │ EC2 │
│ AZ1 │      │ AZ2 │
└──┬──┘      └──┬──┘
   │            │
   └─────┬──────┘
         ▼
    ┌─────────┐
    │RDS      │
    │Multi-AZ │
    └─────────┘
```

### Steps

#### 1. VPC Setup
```bash
# Create VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=my-app-vpc}]'

# Create subnets
aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.0.1.0/24 --availability-zone us-east-1a
aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.0.2.0/24 --availability-zone us-east-1b

# Create Internet Gateway
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway --vpc-id vpc-xxx --internet-gateway-id igw-xxx
```

#### 2. Security Groups
```bash
# Web server security group
aws ec2 create-security-group --group-name web-sg --description "Web servers" --vpc-id vpc-xxx

# Allow HTTP/HTTPS
aws ec2 authorize-security-group-ingress --group-id sg-xxx --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id sg-xxx --protocol tcp --port 443 --cidr 0.0.0.0/0

# Database security group
aws ec2 create-security-group --group-name db-sg --description "Database" --vpc-id vpc-xxx
aws ec2 authorize-security-group-ingress --group-id sg-xxx --protocol tcp --port 5432 --source-group web-sg
```

#### 3. RDS Database
```bash
aws rds create-db-instance \
  --db-instance-identifier myapp-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password SecurePassword123! \
  --allocated-storage 20 \
  --vpc-security-group-ids sg-xxx \
  --db-subnet-group-name my-db-subnet \
  --multi-az
```

#### 4. S3 for Static Assets
```bash
# Create bucket
aws s3 mb s3://myapp-static-assets

# Enable website hosting
aws s3 website s3://myapp-static-assets --index-document index.html

# Sync static files
aws s3 sync ./static/ s3://myapp-static-assets/

# Set bucket policy for public read
aws s3api put-bucket-policy --bucket myapp-static-assets --policy file://bucket-policy.json
```

#### 5. EC2 Launch Template
```bash
# Create launch template
aws ec2 create-launch-template \
  --launch-template-name myapp-template \
  --version-description "Version 1" \
  --launch-template-data file://launch-template.json
```

#### 6. Application Load Balancer
```bash
# Create ALB
aws elbv2 create-load-balancer \
  --name myapp-alb \
  --subnets subnet-xxx subnet-yyy \
  --security-groups sg-xxx

# Create target group
aws elbv2 create-target-group \
  --name myapp-targets \
  --protocol HTTP \
  --port 80 \
  --vpc-id vpc-xxx

# Create listener
aws elbv2 create-listener \
  --load-balancer-arn arn:aws:elasticloadbalancing:... \
  --protocol HTTP \
  --port 80 \
  --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:...
```

#### 7. Auto Scaling Group
```bash
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name myapp-asg \
  --launch-template LaunchTemplateName=myapp-template \
  --min-size 2 \
  --max-size 6 \
  --desired-capacity 2 \
  --target-group-arns arn:aws:elasticloadbalancing:... \
  --vpc-zone-identifier "subnet-xxx,subnet-yyy"
```

---

## 🔴 Project 4: Full DevOps Pipeline with EKS

**Technologies:** Docker, Kubernetes (EKS), AWS, Terraform, CI/CD  
**Time:** 8+ hours  
**Difficulty:** Advanced

### Goal
Build a complete production-ready deployment pipeline.

### Architecture
```
GitHub
  │
  ▼
GitHub Actions
  │
  ├─── Build Docker Image
  ├─── Push to ECR
  ├─── Run Tests
  └─── Deploy to EKS
         │
         ▼
    ┌─────────────────┐
    │   AWS EKS       │
    │  ┌───────────┐  │
    │  │  Ingress  │  │
    │  └─────┬─────┘  │
    │        │        │
    │  ┌─────▼─────┐  │
    │  │   Apps    │  │
    │  └───────────┘  │
    └─────────────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌──────┐  ┌──────┐
│ RDS  │  │  S3  │
└──────┘  └──────┘
```

### Components

1. **Infrastructure as Code (Terraform)**
   - VPC with public/private subnets
   - EKS cluster
   - RDS database
   - S3 buckets
   - IAM roles and policies

2. **Application**
   - Microservices architecture
   - Helm charts for deployment
   - Service mesh (Istio)
   - Monitoring (Prometheus/Grafana)

3. **CI/CD Pipeline**
   - Automated testing
   - Docker image building
   - Security scanning
   - Blue-green deployment

4. **Observability**
   - Centralized logging (ELK stack)
   - Metrics (Prometheus)
   - Distributed tracing (Jaeger)
   - Alerts (AlertManager)

### Key Files

See `projects/04-full-devops-pipeline/` for complete implementation.

---

## 📋 Project Completion Checklist

For each project, ensure you:

- [ ] Understand the architecture
- [ ] Can build and run locally
- [ ] Code is documented
- [ ] Environment variables configured
- [ ] Tests are passing
- [ ] Application is accessible
- [ ] Can scale up/down
- [ ] Logs are viewable
- [ ] Monitoring is set up
- [ ] Clean up resources after

---

## 💡 Tips for Project Success

### 1. Start Small
Don't try to build everything at once. Start with basic functionality and iterate.

### 2. Version Control
Use Git from day one:
```bash
git init
git add .
git commit -m "Initial commit"
```

### 3. Document As You Go
Create a README.md with:
- What the project does
- How to run it
- Architecture diagram
- Environment variables needed
- Troubleshooting guide

### 4. Test Locally First
Before deploying to cloud:
- Test with Docker Compose
- Test on local Kubernetes (Minikube)
- Ensure everything works

### 5. Monitor Costs
When using AWS:
- Set up billing alerts
- Use free tier services
- Delete resources when not in use
- Use t2.micro/t3.micro instances

### 6. Security Best Practices
- Don't commit secrets
- Use environment variables
- Implement proper IAM roles
- Enable MFA
- Use security groups properly

---

## 🎯 Challenge Yourself

Once you complete the projects above, try these enhancements:

### Level Up: Add Caching
- Add Redis for session storage
- Implement CDN caching
- Database query caching

### Level Up: Add Monitoring
- Set up Prometheus + Grafana
- Implement health checks
- Create custom dashboards
- Set up alerts

### Level Up: Add CI/CD
- GitHub Actions workflow
- Automated testing
- Docker image scanning
- Automated deployment

### Level Up: Add Security
- Implement SSL/TLS
- Add authentication (JWT)
- Set up WAF rules
- Implement rate limiting
- Secret management (Vault)

### Level Up: Multi-Region
- Deploy to multiple AWS regions
- Set up Route 53 routing
- Database replication
- Global CDN

---

## 📚 Additional Project Ideas

1. **E-commerce Platform**
   - Product catalog
   - Shopping cart
   - Payment processing
   - Order management

2. **Social Media App**
   - User authentication
   - Post creation/feed
   - Real-time notifications
   - Image uploads to S3

3. **Data Pipeline**
   - Data ingestion (Kafka)
   - Stream processing
   - Data warehouse
   - Analytics dashboard

4. **IoT Platform**
   - Device management
   - MQTT broker
   - Time-series database
   - Real-time analytics

5. **SaaS Application**
   - Multi-tenancy
   - Subscription management
   - Usage metering
   - Admin dashboard

---

## 🎓 Learning Resources

- **Project Templates:** `projects/templates/`
- **Code Examples:** Each project folder
- **Video Tutorials:** Links in project READMEs
- **Community Projects:** GitHub awesome lists

---

**Remember:** The goal is not to build perfect projects, but to learn by doing. Make mistakes, break things, and learn from them!

Happy building! 🚀

