# ☁️ AWS - Advanced Level

Master AWS architectures for enterprise and production systems!

---

## 📚 Table of Contents

1. [Advanced Architectures](#advanced-architectures)
2. [Microservices on AWS](#microservices-aws)
3. [High Availability & DR](#ha-dr)
4. [Security & Compliance](#security-compliance)
5. [Cost Optimization](#cost-optimization)
6. [DevOps & CI/CD](#devops-cicd)
7. [Advanced Networking](#advanced-networking)
8. [Interview Questions](#interview-questions)

---

## 🏛️ Advanced Architectures

### Well-Architected Framework

**Five Pillars:**

```yaml
1. Operational Excellence:
   - IaC (CloudFormation, Terraform)
   - CI/CD pipelines
   - Monitoring and logging
   - Incident response

2. Security:
   - Identity and access management
   - Detective controls
   - Infrastructure protection
   - Data protection

3. Reliability:
   - Recover from failures
   - Horizontal scaling
   - Automated recovery
   - Testing recovery procedures

4. Performance Efficiency:
   - Right-sizing resources
   - Monitoring performance
   - Trade-offs (consistency vs latency)

5. Cost Optimization:
   - Pay only for what you use
   - Right-sizing
   - Reserved Instances
   - Spot Instances
```

### Three-Tier Web Application Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                     AWS Cloud                                 │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Presentation Tier                       │    │
│  │  ┌────────────────────────────────────────────┐     │    │
│  │  │ CloudFront CDN                             │     │    │
│  │  │ - Edge Locations                           │     │    │
│  │  │ - Static Content Caching                   │     │    │
│  │  └────────────────────────────────────────────┘     │    │
│  │  ┌────────────────────────────────────────────┐     │    │
│  │  │ Route 53 DNS                               │     │    │
│  │  │ - Health Checks                            │     │    │
│  │  │ - Traffic Routing                          │     │    │
│  │  └────────────────────────────────────────────┘     │    │
│  └─────────────────────────────────────────────────────┘    │
│                          ↓                                   │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Application Tier                        │    │
│  │  ┌────────────────────────────────────────────┐     │    │
│  │  │ Application Load Balancer                  │     │    │
│  │  └────────────────────────────────────────────┘     │    │
│  │           ↓              ↓              ↓            │    │
│  │  [AZ-1: Web Tier] [AZ-2: Web Tier] [AZ-3: Web Tier]│    │
│  │  ┌──────────┐      ┌──────────┐      ┌──────────┐  │    │
│  │  │ ASG      │      │ ASG      │      │ ASG      │  │    │
│  │  │ EC2/ECS  │      │ EC2/ECS  │      │ EC2/ECS  │  │    │
│  │  └──────────┘      └──────────┘      └──────────┘  │    │
│  │           ↓              ↓              ↓            │    │
│  │  ┌────────────────────────────────────────────┐     │    │
│  │  │ Application Load Balancer (Internal)       │     │    │
│  │  └────────────────────────────────────────────┘     │    │
│  │           ↓              ↓              ↓            │    │
│  │  [AZ-1: App Tier] [AZ-2: App Tier] [AZ-3: App Tier]│    │
│  │  ┌──────────┐      ┌──────────┐      ┌──────────┐  │    │
│  │  │ ASG      │      │ ASG      │      │ ASG      │  │    │
│  │  │ EC2/ECS  │      │ EC2/ECS  │      │ EC2/ECS  │  │    │
│  │  └──────────┘      └──────────┘      └──────────┘  │    │
│  └─────────────────────────────────────────────────────┘    │
│                          ↓                                   │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Data Tier                               │    │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐    │    │
│  │  │ RDS Multi-AZ                │  │ ElastiCache│    │    │
│  │  │ Primary    │→ │ Standby    │  │ Redis/     │    │    │
│  │  │ (AZ-1)     │  │ (AZ-2)     │  │ Memcached  │    │    │
│  │  └────────────┘  └────────────┘  └────────────┘    │    │
│  │  ┌────────────────────────────────────────────┐     │    │
│  │  │ S3 Buckets (Static Assets, Backups)       │     │    │
│  │  └────────────────────────────────────────────┘     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │   Monitoring & Security                              │    │
│  │   - CloudWatch (Logs, Metrics, Alarms)              │    │
│  │   - CloudTrail (Audit Logs)                          │    │
│  │   - AWS Config (Compliance)                          │    │
│  │   - GuardDuty (Threat Detection)                     │    │
│  │   - WAF (Web Application Firewall)                   │    │
│  │   - Secrets Manager (Credentials)                    │    │
│  └─────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

---

## 🔬 Microservices on AWS

### Containerized Microservices with ECS/EKS

```yaml
Architecture Components:

1. Container Orchestration:
   - ECS (Elastic Container Service)
     • AWS-native
     • Tight AWS integration
     • Simpler setup
   
   - EKS (Elastic Kubernetes Service)
     • Kubernetes-based
     • Portable across clouds
     • Rich ecosystem

2. Service Discovery:
   - AWS Cloud Map
   - Route 53 private hosted zones
   - ECS Service Discovery

3. Load Balancing:
   - ALB for HTTP/HTTPS
   - NLB for TCP/UDP
   - App Mesh for service mesh

4. Storage:
   - EFS for shared storage
   - EBS for persistent volumes
   - S3 for object storage

5. Secrets Management:
   - AWS Secrets Manager
   - Parameter Store
   - Injected as environment variables

6. CI/CD:
   - CodePipeline
   - CodeBuild
   - CodeDeploy
   - ECR (Container Registry)
```

**Example: ECS Fargate Service**

```yaml
# ECS Task Definition
{
  "family": "api-service",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "containerDefinitions": [
    {
      "name": "api-container",
      "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/api:latest",
      "portMappings": [
        {
          "containerPort": 8080,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "DB_HOST",
          "value": "mydb.cluster-xxx.us-east-1.rds.amazonaws.com"
        }
      ],
      "secrets": [
        {
          "name": "DB_PASSWORD",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:123:secret:db-pass"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/api-service",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "api"
        }
      }
    }
  ]
}
```

### API Gateway Patterns

```yaml
Use Cases:

1. REST API:
   - RESTful endpoints
   - Lambda integration
   - Request/response transformation
   - Caching
   - Throttling & rate limiting

2. HTTP API:
   - Lower latency
   - Lower cost
   - JWT authorization
   - CORS support

3. WebSocket API:
   - Real-time communication
   - Bidirectional
   - Chat applications
   - Live dashboards

Features:
  - Custom domain names
  - API keys
  - Usage plans & quotas
  - Request validation
  - WAF integration
  - CloudWatch logging
  - X-Ray tracing
```

---

## 🛡️ High Availability & Disaster Recovery

### Disaster Recovery Strategies

```yaml
1. Backup & Restore (RPO: hours, RTO: hours):
   Cost: $
   - Regular backups to S3
   - Restore when disaster occurs
   Use: Non-critical workloads

2. Pilot Light (RPO: minutes, RTO: 10s minutes):
   Cost: $$
   - Core infrastructure always running
   - Scale up during disaster
   Use: Critical workloads

3. Warm Standby (RPO: seconds, RTO: minutes):
   Cost: $$$
   - Scaled-down version always running
   - Scale up during disaster
   Use: Business-critical workloads

4. Multi-Site Active/Active (RPO: none, RTO: none):
   Cost: $$$$
   - Full environment in multiple regions
   - Traffic distributed across all sites
   Use: Mission-critical workloads
```

**Multi-Region Architecture Example:**

```yaml
Primary Region (us-east-1):
  - Route 53 with health checks
  - Full application stack
  - RDS Primary
  - S3 with cross-region replication
  - DynamoDB Global Tables

Secondary Region (us-west-2):
  - Standby application stack
  - RDS Read Replica (can be promoted)
  - S3 replicated
  - DynamoDB Global Tables

Failover Process:
  1. Route 53 detects primary failure
  2. Automatic DNS failover to secondary
  3. Promote RDS read replica if needed
  4. Scale up secondary region resources
```

---

## 🔒 Security & Compliance

### Defense in Depth Strategy

```yaml
Layer 1: Edge Security
  - AWS Shield (DDoS protection)
  - WAF (Web Application Firewall)
  - CloudFront with signed URLs/cookies

Layer 2: Network Security
  - VPC with private subnets
  - Security groups (allow-list)
  - Network ACLs (allow/deny)
  - VPC Flow Logs
  - PrivateLink for AWS services

Layer 3: Identity & Access
  - IAM with least privilege
  - MFA for privileged users
  - Roles instead of long-term credentials
  - Cognito for user authentication
  - SSO integration

Layer 4: Application Security
  - Secrets Manager for credentials
  - Parameter Store for config
  - KMS for encryption keys
  - Certificate Manager for SSL/TLS
  - Code signing

Layer 5: Data Security
  - Encryption at rest (S3, EBS, RDS)
  - Encryption in transit (TLS/SSL)
  - S3 bucket policies
  - RDS encryption
  - Backup encryption

Layer 6: Monitoring & Response
  - CloudTrail (audit logs)
  - CloudWatch (monitoring)
  - Config (compliance)
  - GuardDuty (threat detection)
  - Security Hub (central dashboard)
  - Macie (sensitive data discovery)
```

**Example: Secure S3 Bucket Configuration**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnencryptedObjectUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::my-bucket/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "AES256"
        }
      }
    },
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

---

## 💰 Cost Optimization

### Cost Optimization Strategies

```yaml
1. Right-Sizing:
   - Use CloudWatch metrics
   - Identify underutilized resources
   - Downsize or terminate
   - Use AWS Compute Optimizer

2. Purchase Options:
   - Reserved Instances (1-3 years)
   - Savings Plans (flexible)
   - Spot Instances (fault-tolerant workloads)
   - On-Demand (unpredictable workloads)

3. Storage Optimization:
   - S3 Intelligent-Tiering
   - Lifecycle policies
   - EBS volume optimization
   - Delete unused snapshots

4. Auto Scaling:
   - Scale based on demand
   - Scheduled scaling
   - Predictive scaling

5. Monitoring & Alerts:
   - AWS Cost Explorer
   - AWS Budgets
   - Cost anomaly detection
   - Tag-based cost allocation

6. Architecture Optimization:
   - Serverless where appropriate
   - Managed services
   - Content delivery (CloudFront)
   - Data transfer optimization
```

**S3 Lifecycle Policy Example:**

```json
{
  "Rules": [
    {
      "Id": "Archive old logs",
      "Status": "Enabled",
      "Prefix": "logs/",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        },
        {
          "Days": 365,
          "StorageClass": "DEEP_ARCHIVE"
        }
      ],
      "Expiration": {
        "Days": 2555
      }
    }
  ]
}
```

---

## 🚀 DevOps & CI/CD

### Complete CI/CD Pipeline

```yaml
Pipeline Stages:

1. Source:
   - CodeCommit / GitHub / Bitbucket
   - Webhook triggers on push
   - Branch strategies (GitFlow)

2. Build:
   - CodeBuild
   - Run unit tests
   - Code quality checks (SonarQube)
   - Security scanning
   - Build artifacts
   - Push to ECR

3. Test:
   - Deploy to test environment
   - Integration tests
   - Load tests
   - Security tests

4. Approval:
   - Manual approval gate
   - SNS notification
   - Review metrics

5. Deploy:
   - Blue/Green deployment
   - Canary deployment
   - Rolling deployment
   - CloudFormation/CDK

6. Monitor:
   - CloudWatch alarms
   - X-Ray tracing
   - Rollback on failure
```

**CodePipeline Example:**

```yaml
version: 0.2

phases:
  install:
    runtime-versions:
      java: corretto11
    commands:
      - echo Installing dependencies
      - apt-get update
      - apt-get install -y maven
  
  pre_build:
    commands:
      - echo Logging in to Amazon ECR
      - aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPOSITORY
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}
  
  build:
    commands:
      - echo Build started on `date`
      - mvn clean package
      - docker build -t $ECR_REPOSITORY:latest .
      - docker tag $ECR_REPOSITORY:latest $ECR_REPOSITORY:$IMAGE_TAG
  
  post_build:
    commands:
      - echo Build completed on `date`
      - docker push $ECR_REPOSITORY:latest
      - docker push $ECR_REPOSITORY:$IMAGE_TAG
      - echo Writing image definitions file
      - printf '[{"name":"my-app","imageUri":"%s"}]' $ECR_REPOSITORY:$IMAGE_TAG > imagedefinitions.json

artifacts:
  files:
    - imagedefinitions.json
    - appspec.yaml
```

---

## 🌐 Advanced Networking

### Transit Gateway Architecture

```yaml
Transit Gateway Use Cases:
  - Connect multiple VPCs
  - Hub-and-spoke topology
  - On-premises connectivity
  - Inter-region peering

Benefits:
  - Centralized routing
  - Simplified network architecture
  - Scalability (5000+ attachments)
  - Bandwidth aggregation

Components:
  - VPC attachments
  - VPN attachments
  - Direct Connect attachments
  - Peering attachments
  - Route tables
```

### Direct Connect

```yaml
Features:
  - Dedicated network connection
  - 1 Gbps or 10 Gbps
  - Bypass internet
  - Lower latency
  - Consistent network performance
  - Access public and private resources

Use Cases:
  - Large data transfers
  - Real-time data feeds
  - Hybrid cloud
  - Disaster recovery

Setup:
  1. Choose Direct Connect location
  2. Create virtual interface
  3. Configure BGP
  4. Test connectivity
  5. Cut over traffic
```

---

## 🎯 Interview Questions

### Advanced AWS Scenarios

**Q1: Design a highly available and scalable web application**

**Answer:**
- Multi-AZ deployment
- Auto Scaling Groups in multiple AZs
- Application Load Balancer
- RDS Multi-AZ or Aurora
- ElastiCache for session storage
- S3 + CloudFront for static content
- Route 53 for DNS with health checks
- CloudWatch for monitoring
- WAF for security

**Q2: How would you migrate a monolithic application to microservices on AWS?**

**Answer:**
1. Decompose monolith by business capability
2. Use ECS/EKS for container orchestration
3. API Gateway for API management
4. Service mesh (App Mesh) for inter-service communication
5. DynamoDB/RDS for data stores
6. SQS/SNS for async communication
7. Implement CI/CD pipeline
8. Gradual migration (strangler pattern)

**Q3: Implement a multi-region disaster recovery strategy**

**Answer:**
- Primary region with full stack
- Secondary region with pilot light/warm standby
- Route 53 with health checks for failover
- RDS cross-region read replicas
- S3 cross-region replication
- DynamoDB Global Tables
- Lambda@Edge for edge computing
- Regular DR testing and runbooks

---

**You're now ready for AWS Solutions Architect & DevOps roles!** 🚀

