# ☁️ AWS Beginner Guide

## What is AWS?

Amazon Web Services (AWS) is a comprehensive cloud computing platform offering over 200 services including computing power, storage, databases, networking, and more.

### Why AWS?

**Benefits:**
- ✅ Pay only for what you use
- ✅ Scale up or down instantly
- ✅ Global infrastructure
- ✅ Enterprise-grade security
- ✅ Vast service ecosystem
- ✅ Industry leader (32% market share)

---

## 🌍 AWS Global Infrastructure

```
┌─────────────────────────────────────────┐
│           AWS Global Network            │
├─────────────────────────────────────────┤
│  Regions (31+)                          │
│  └─ Availability Zones (99+)            │
│     └─ Data Centers                     │
│                                         │
│  Edge Locations (400+)                  │
│  └─ CloudFront CDN                      │
└─────────────────────────────────────────┘
```

### Key Concepts

- **Region:** Geographic area (e.g., us-east-1, eu-west-1)
- **Availability Zone (AZ):** Isolated data centers within a region
- **Edge Location:** CDN endpoints for content delivery

---

## 🚀 Getting Started

### Step 1: Create AWS Account

1. Go to [aws.amazon.com](https://aws.amazon.com)
2. Click "Create an AWS Account"
3. Provide email, password, account name
4. Enter payment information (required but free tier available)
5. Verify identity (phone/SMS)
6. Select Basic Support Plan (Free)

### Step 2: Understanding AWS Free Tier

AWS offers three types of free tier:

**Always Free**
- Lambda: 1M requests/month
- DynamoDB: 25GB storage
- CloudWatch: 10 custom metrics

**12 Months Free**
- EC2: 750 hours/month (t2.micro)
- S3: 5GB storage
- RDS: 750 hours/month (db.t2.micro)

**Trials**
- Various services with short trial periods

⚠️ **Important:** Monitor usage to avoid charges!

### Step 3: Secure Your Account

```
Root Account (Created by default)
└─ Enable MFA (Multi-Factor Authentication)
└─ Don't use for daily tasks
└─ Create IAM users instead
```

---

## 🔐 IAM (Identity and Access Management)

IAM controls who can access your AWS resources.

### Key Concepts

- **Users:** Individual accounts
- **Groups:** Collection of users
- **Roles:** Temporary permissions for services
- **Policies:** JSON documents defining permissions

### Creating Your First IAM User

**Via Console:**

1. Go to IAM Dashboard
2. Click "Users" → "Add User"
3. Set username
4. Select access type:
   - ✅ Programmatic access (API, CLI)
   - ✅ AWS Management Console access
5. Set permissions:
   - Attach AdministratorAccess (for learning)
6. Create user
7. **Download credentials** (only chance!)

### IAM Best Practices

- ✅ Never use root account for daily tasks
- ✅ Enable MFA for root and IAM users
- ✅ Create individual IAM users
- ✅ Use groups to assign permissions
- ✅ Grant least privilege
- ✅ Rotate credentials regularly
- ✅ Use roles for EC2 instances

### Sample IAM Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 💻 AWS CLI Setup

### Installation

**Windows:**
```bash
# Using MSI installer
Download from: https://aws.amazon.com/cli/

# Or using pip
pip install awscli
```

**macOS:**
```bash
brew install awscli
```

**Linux:**
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

### Configuration

```bash
# Configure AWS CLI
aws configure

# You'll be prompted for:
AWS Access Key ID: [Your Access Key]
AWS Secret Access Key: [Your Secret Key]
Default region name: us-east-1
Default output format: json

# Test configuration
aws sts get-caller-identity

# Output:
{
    "UserId": "AIDAXXXXXXXXXXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/myuser"
}
```

### Essential AWS CLI Commands

```bash
# List S3 buckets
aws s3 ls

# List EC2 instances
aws ec2 describe-instances

# Get AWS regions
aws ec2 describe-regions

# Get account ID
aws sts get-caller-identity --query Account --output text

# Configure named profile
aws configure --profile dev

# Use specific profile
aws s3 ls --profile dev
```

---

## 🖥️ EC2 (Elastic Compute Cloud)

Virtual servers in the cloud.

### Instance Types

| Type | Use Case | Example |
|------|----------|---------|
| **t2.micro** | Free tier, testing | Small websites |
| **t3.medium** | General purpose | Web applications |
| **m5.large** | Balanced compute/memory | Databases |
| **c5.xlarge** | Compute optimized | Scientific computing |
| **r5.2xlarge** | Memory optimized | In-memory databases |

### Launching Your First EC2 Instance

**Via Console:**

1. **Navigate to EC2**
   - Search "EC2" in AWS Console
   - Click "Launch Instance"

2. **Choose AMI (Amazon Machine Image)**
   - Amazon Linux 2 (Free tier eligible)
   - Ubuntu Server
   - Windows Server

3. **Choose Instance Type**
   - t2.micro (Free tier)

4. **Configure Instance**
   - Number of instances: 1
   - Network: Default VPC
   - Auto-assign Public IP: Enable

5. **Add Storage**
   - 8 GB (Free tier: up to 30 GB)

6. **Add Tags**
   - Key: Name
   - Value: MyFirstEC2

7. **Configure Security Group**
   - SSH (port 22) - Your IP only
   - HTTP (port 80) - Anywhere
   - HTTPS (port 443) - Anywhere

8. **Review and Launch**
   - Create or select key pair
   - **Download key pair** (.pem file)
   - Launch!

### Connecting to EC2

**Linux/Mac:**
```bash
# Set key permissions
chmod 400 my-key.pem

# Connect via SSH
ssh -i my-key.pem ec2-user@<public-ip>

# For Ubuntu
ssh -i my-key.pem ubuntu@<public-ip>
```

**Windows (PowerShell):**
```bash
# Using PuTTY or native SSH
ssh -i my-key.pem ec2-user@<public-ip>
```

### Installing Web Server on EC2

```bash
# Update packages
sudo yum update -y  # Amazon Linux
sudo apt update -y  # Ubuntu

# Install Apache
sudo yum install httpd -y  # Amazon Linux
sudo apt install apache2 -y  # Ubuntu

# Start Apache
sudo systemctl start httpd  # Amazon Linux
sudo systemctl start apache2  # Ubuntu

# Enable on boot
sudo systemctl enable httpd

# Create simple page
echo "<h1>Hello from AWS EC2!</h1>" | sudo tee /var/www/html/index.html

# Visit: http://<public-ip>
```

### EC2 User Data (Automation)

Launch script that runs on first boot:

```bash
#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
echo "<h1>Deployed via User Data</h1>" > /var/www/html/index.html
```

---

## 🗄️ S3 (Simple Storage Service)

Object storage service for any type of data.

### Key Concepts

- **Bucket:** Container for objects (globally unique name)
- **Object:** File + metadata (up to 5TB)
- **Key:** Object name/path
- **Versioning:** Keep multiple versions of objects
- **Durability:** 99.999999999% (11 nines)

### Storage Classes

| Class | Use Case | Cost |
|-------|----------|------|
| **Standard** | Frequently accessed | $$$$ |
| **Intelligent-Tiering** | Auto-tiering | $$$ |
| **Standard-IA** | Infrequent access | $$ |
| **Glacier** | Archive | $ |
| **Glacier Deep Archive** | Long-term archive | ¢ |

### Creating S3 Bucket (CLI)

```bash
# Create bucket
aws s3 mb s3://my-unique-bucket-name-12345

# List buckets
aws s3 ls

# Upload file
aws s3 cp myfile.txt s3://my-unique-bucket-name-12345/

# Download file
aws s3 cp s3://my-unique-bucket-name-12345/myfile.txt ./

# Sync directory
aws s3 sync ./my-folder s3://my-unique-bucket-name-12345/folder/

# List objects in bucket
aws s3 ls s3://my-unique-bucket-name-12345/

# Delete object
aws s3 rm s3://my-unique-bucket-name-12345/myfile.txt

# Delete bucket (must be empty)
aws s3 rb s3://my-unique-bucket-name-12345
```

### S3 Static Website Hosting

```bash
# Enable static website hosting
aws s3 website s3://my-bucket/ --index-document index.html

# Upload website files
aws s3 sync ./website/ s3://my-bucket/ --acl public-read

# Bucket policy for public access
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}

# Website URL:
# http://my-bucket.s3-website-us-east-1.amazonaws.com
```

---

## 🌐 VPC (Virtual Private Cloud)

Your private network in AWS.

### VPC Components

```
VPC (10.0.0.0/16)
├── Public Subnet (10.0.1.0/24)
│   ├── Web Servers
│   └── Internet Gateway
├── Private Subnet (10.0.2.0/24)
│   ├── App Servers
│   └── NAT Gateway
└── Private Subnet (10.0.3.0/24)
    └── Databases
```

### Key Concepts

- **VPC:** Isolated network
- **Subnet:** Range of IP addresses
- **Internet Gateway:** Connect to internet
- **NAT Gateway:** Private subnet internet access
- **Route Table:** Traffic routing rules
- **Security Group:** Instance-level firewall
- **Network ACL:** Subnet-level firewall

### Default VPC

- Created automatically in each region
- Public subnet in each AZ
- Internet Gateway attached
- Good for getting started

### Security Groups

**Inbound Rules:**
```
Type        Protocol    Port    Source
SSH         TCP         22      My IP (203.0.113.0/32)
HTTP        TCP         80      Anywhere (0.0.0.0/0)
HTTPS       TCP         443     Anywhere (0.0.0.0/0)
Custom TCP  TCP         3000    Security Group ID
```

**Key Points:**
- Stateful (return traffic automatic)
- Default: Deny all inbound, allow all outbound
- Best practice: Least privilege

---

## 💾 RDS (Relational Database Service)

Managed database service.

### Supported Engines

- Amazon Aurora
- PostgreSQL
- MySQL
- MariaDB
- Oracle
- SQL Server

### Creating RDS Instance

**Via Console:**

1. Go to RDS Dashboard
2. Click "Create database"
3. Choose creation method: Standard
4. Engine: PostgreSQL (or MySQL)
5. Templates: Free tier
6. Settings:
   - DB instance identifier: my-database
   - Master username: admin
   - Master password: [secure password]
7. Instance configuration: db.t2.micro
8. Storage: 20 GB GP2
9. Connectivity:
   - VPC: Default
   - Public access: Yes (for learning)
   - Security group: Create new
10. Create database

### Connecting to RDS

```bash
# PostgreSQL
psql -h database-endpoint.rds.amazonaws.com -U admin -d postgres

# MySQL
mysql -h database-endpoint.rds.amazonaws.com -u admin -p
```

### RDS Best Practices

- ✅ Enable Multi-AZ for production
- ✅ Enable automated backups
- ✅ Use read replicas for scaling
- ✅ Never expose to internet (use VPC)
- ✅ Encrypt at rest and in transit
- ✅ Regular security patches (auto)

---

## 🎯 Hands-On Project: Deploy Web Application

Let's deploy a complete web application!

### Architecture

```
Internet
    ↓
Load Balancer
    ↓
EC2 (Web Server)
    ↓
RDS (Database)
    ↓
S3 (Static Assets)
```

### Step-by-Step

**1. Create VPC and Subnets**
```bash
# Use default VPC for simplicity
aws ec2 describe-vpcs
```

**2. Create Security Groups**
```bash
# Web server security group
aws ec2 create-security-group \
  --group-name web-sg \
  --description "Web server security group"

# Allow HTTP
aws ec2 authorize-security-group-ingress \
  --group-name web-sg \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```

**3. Create S3 Bucket for Static Assets**
```bash
aws s3 mb s3://my-app-assets-12345
aws s3 sync ./static/ s3://my-app-assets-12345/
```

**4. Launch EC2 Instance**
```bash
# Create key pair
aws ec2 create-key-pair \
  --key-name my-app-key \
  --query 'KeyMaterial' \
  --output text > my-app-key.pem

chmod 400 my-app-key.pem

# Launch instance
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name my-app-key \
  --security-groups web-sg \
  --user-data file://install-web.sh
```

**5. Create RDS Database**
```bash
aws rds create-db-instance \
  --db-instance-identifier my-app-db \
  --db-instance-class db.t2.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password SecurePassword123 \
  --allocated-storage 20
```

**6. Deploy Application**
```bash
# SSH to EC2
ssh -i my-app-key.pem ec2-user@<public-ip>

# Install Node.js
curl -sL https://rpm.nodesource.com/setup_16.x | sudo bash -
sudo yum install -y nodejs

# Clone your app
git clone https://github.com/your-app.git
cd your-app

# Install dependencies
npm install

# Set environment variables
export DB_HOST=<rds-endpoint>
export DB_USER=admin
export DB_PASS=SecurePassword123

# Start application
npm start
```

---

## 📊 CloudWatch (Monitoring)

AWS monitoring and observability service.

### Key Features

- Metrics: CPU, network, disk
- Logs: Application and system logs
- Alarms: Notifications based on thresholds
- Dashboards: Visualize metrics

### Creating CloudWatch Alarm

```bash
# CPU alarm
aws cloudwatch put-metric-alarm \
  --alarm-name high-cpu \
  --alarm-description "CPU usage exceeds 80%" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --evaluation-periods 2 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold
```

---

## 💰 Cost Management

### Best Practices

1. **Use Free Tier**
   - Monitor free tier usage
   - Set up billing alerts

2. **Cost Explorer**
   - Analyze spending patterns
   - Identify cost drivers

3. **Budgets**
   - Set monthly budgets
   - Get alerts before overspending

4. **Resource Cleanup**
   - Stop unused EC2 instances
   - Delete old snapshots
   - Remove unused load balancers

### Setting Up Billing Alert

```bash
# Create SNS topic for alerts
aws sns create-topic --name billing-alerts

# Subscribe email
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:billing-alerts \
  --protocol email \
  --notification-endpoint your-email@example.com

# Create budget
aws budgets create-budget \
  --account-id 123456789012 \
  --budget file://budget.json
```

---

## ✅ Beginner Checklist

- [ ] AWS account created
- [ ] MFA enabled on root account
- [ ] IAM user created
- [ ] AWS CLI installed and configured
- [ ] Launched and connected to EC2 instance
- [ ] Created S3 bucket and uploaded files
- [ ] Understand VPC basics
- [ ] Created RDS database
- [ ] Set up billing alerts
- [ ] Understand AWS Free Tier limits

---

## 🚀 Next Steps

You've learned AWS basics!

Move to: `aws/02-intermediate/`

**Next Topics:**
- Load Balancers (ALB/NLB)
- Auto Scaling
- Lambda Functions
- API Gateway
- CloudFormation
- Advanced VPC

---

## 📚 Additional Resources

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS Training](https://aws.amazon.com/training/)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)

Good luck with your AWS journey! ☁️

