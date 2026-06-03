# ☁️ AWS - Intermediate Level

Master AWS services and architectures for real-world applications!

---

## 📚 Table of Contents

1. [Advanced EC2](#advanced-ec2)
2. [Load Balancing & Auto Scaling](#load-balancing)
3. [RDS & Database Services](#rds-databases)
4. [VPC Networking](#vpc-networking)
5. [IAM Advanced](#iam-advanced)
6. [CloudFormation](#cloudformation)
7. [Lambda & Serverless](#lambda-serverless)
8. [Interview Questions](#interview-questions)

---

## 🖥️ Advanced EC2

### Q1: EC2 Instance Types & Selection

**Answer:**

**Instance Families:**

```
GENERAL PURPOSE (T, M)
├── T2/T3/T3a - Burstable performance
│   Use: Web servers, dev environments
├── M5/M6 - Balanced compute/memory
    Use: Application servers, databases

COMPUTE OPTIMIZED (C)
├── C5/C6 - High CPU performance
    Use: Batch processing, gaming servers

MEMORY OPTIMIZED (R, X, Z)
├── R5/R6 - Memory-intensive applications
│   Use: In-memory databases, big data
├── X1/X2 - Extreme memory
    Use: SAP HANA, in-memory databases

STORAGE OPTIMIZED (I, D, H)
├── I3/I4 - High IOPS, NVMe SSD
│   Use: NoSQL databases, data warehousing
├── D2/D3 - Dense HDD storage
    Use: MapReduce, distributed file systems

ACCELERATED COMPUTING (P, G, F)
├── P3/P4 - GPU instances
│   Use: ML training, HPC
├── G4 - Graphics workloads
    Use: Gaming, rendering
```

**Purchasing Options:**

```bash
# 1. On-Demand - Pay by hour/second
# Use: Short-term, unpredictable workloads

# 2. Reserved Instances - 1 or 3 year commitment
# Savings: Up to 75%
# Use: Steady-state workloads

# 3. Spot Instances - Bid for unused capacity
# Savings: Up to 90%
# Use: Fault-tolerant, flexible workloads

# 4. Savings Plans - Flexible commitment
# Savings: Up to 72%
# Use: Consistent usage patterns

# 5. Dedicated Hosts - Physical server
# Use: Licensing requirements, compliance
```

### Q2: EC2 User Data & Metadata

**Answer:**

```bash
# User Data - Run scripts at instance launch
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from $(hostname -f)</h1>" > /var/www/html/index.html

# Access instance metadata from within instance
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/latest/meta-data/instance-id
curl http://169.254.169.254/latest/meta-data/public-ipv4
curl http://169.254.169.254/latest/meta-data/placement/availability-zone

# Get user data
curl http://169.254.169.254/latest/user-data
```

---

## ⚖️ Load Balancing & Auto Scaling

### Q3: Elastic Load Balancer Types

**Answer:**

**1. Application Load Balancer (ALB) - Layer 7**

```yaml
Features:
  - HTTP/HTTPS traffic
  - Path-based routing
  - Host-based routing
  - Support for WebSocket
  - Target types: EC2, IP, Lambda

Use Cases:
  - Microservices
  - Container-based applications
  - Advanced request routing

Example Routing:
  - example.com/api/* → API Target Group
  - example.com/images/* → Static Target Group
  - api.example.com → API Target Group
  - www.example.com → Web Target Group
```

**2. Network Load Balancer (NLB) - Layer 4**

```yaml
Features:
  - TCP/UDP traffic
  - Ultra-high performance (millions of requests/sec)
  - Static IP addresses
  - Preserve source IP
  - Low latency

Use Cases:
  - Extreme performance requirements
  - Gaming applications
  - IoT applications
```

**3. Gateway Load Balancer (GWLB)**

```yaml
Features:
  - Deploy third-party virtual appliances
  - Traffic inspection
  - Firewall, IDS/IPS

Use Cases:
  - Security appliances
  - Network monitoring
```

### Q4: Auto Scaling

**Answer:**

```yaml
Auto Scaling Components:
  1. Launch Template/Configuration
     - AMI, instance type, key pair
     - Security groups, IAM role
     - User data script
  
  2. Auto Scaling Group (ASG)
     - Min/Max/Desired capacity
     - VPC and subnets
     - Health checks
     - Load balancer integration
  
  3. Scaling Policies
     - Target Tracking: Maintain metric target
     - Step Scaling: Scale based on CloudWatch alarms
     - Scheduled Scaling: Time-based scaling
     - Predictive Scaling: ML-based forecasting

Example Target Tracking Policy:
  - Maintain average CPU at 50%
  - Maintain request count per target
  - Maintain network throughput
```

**Example ASG Configuration:**

```bash
# Create launch template
aws ec2 create-launch-template \
  --launch-template-name my-template \
  --launch-template-data '{
    "ImageId": "ami-0abcdef1234567890",
    "InstanceType": "t3.micro",
    "KeyName": "my-key",
    "SecurityGroupIds": ["sg-12345678"]
  }'

# Create Auto Scaling Group
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name my-asg \
  --launch-template LaunchTemplateName=my-template \
  --min-size 2 \
  --max-size 10 \
  --desired-capacity 4 \
  --vpc-zone-identifier "subnet-1,subnet-2,subnet-3" \
  --target-group-arns "arn:aws:elasticloadbalancing:..."

# Create target tracking policy
aws autoscaling put-scaling-policy \
  --auto-scaling-group-name my-asg \
  --policy-name cpu-target-tracking \
  --policy-type TargetTrackingScaling \
  --target-tracking-configuration '{
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ASGAverageCPUUtilization"
    },
    "TargetValue": 50.0
  }'
```

---

## 🗄️ RDS & Database Services

### Q5: RDS Features & Best Practices

**Answer:**

**RDS Database Engines:**
- MySQL
- PostgreSQL
- MariaDB
- Oracle
- SQL Server
- Aurora (AWS proprietary)

**Key Features:**

```yaml
1. Automated Backups:
   - Retention: 1-35 days
   - Point-in-time recovery
   - Stored in S3

2. Multi-AZ Deployment:
   - Synchronous replication
   - Automatic failover
   - High availability

3. Read Replicas:
   - Asynchronous replication
   - Scale read workloads
   - Can be in different region

4. Encryption:
   - At-rest: KMS encryption
   - In-transit: SSL/TLS

5. Performance Insights:
   - Monitor database performance
   - Identify bottlenecks
```

**RDS vs Aurora:**

```yaml
RDS:
  Compatibility: MySQL, PostgreSQL
  Performance: Standard
  Storage: Up to 64 TB
  Replicas: Up to 5 read replicas
  Cost: Lower

Aurora:
  Compatibility: MySQL, PostgreSQL compatible
  Performance: 5x MySQL, 3x PostgreSQL
  Storage: Up to 128 TB, auto-scaling
  Replicas: Up to 15 read replicas
  High Availability: 6 copies across 3 AZs
  Cost: ~20% more than RDS
  Features: Serverless, Global Database
```

### Q6: DynamoDB

**Answer:**

**Features:**
- Fully managed NoSQL database
- Single-digit millisecond performance
- Auto-scaling
- Global tables (multi-region)
- On-demand or provisioned capacity

**Key Concepts:**

```javascript
// Table structure
{
  "TableName": "Users",
  "PartitionKey": "userId",  // Required
  "SortKey": "timestamp",    // Optional
  "Attributes": {
    "userId": "string",
    "name": "string",
    "email": "string",
    "timestamp": "number"
  }
}

// Read Consistency
// Eventually Consistent Read (default) - Lower cost
// Strongly Consistent Read - Higher cost, latest data

// Capacity Modes
// 1. On-Demand: Pay per request
// 2. Provisioned: Specify RCU/WCU

// Calculations
// Read Capacity Unit (RCU):
//   - 1 RCU = 1 strongly consistent read/sec (4KB)
//   - 1 RCU = 2 eventually consistent reads/sec (4KB)

// Write Capacity Unit (WCU):
//   - 1 WCU = 1 write/sec (1KB)
```

---

## 🌐 VPC Networking

### Q7: VPC Components

**Answer:**

```
VPC Architecture:
┌─────────────────────────────────────────────────────┐
│                    VPC (10.0.0.0/16)                 │
├─────────────────────────────────────────────────────┤
│  Availability Zone A    │  Availability Zone B      │
│  ┌───────────────────┐  │  ┌───────────────────┐   │
│  │ Public Subnet     │  │  │ Public Subnet     │   │
│  │ 10.0.1.0/24       │  │  │ 10.0.2.0/24       │   │
│  │ - Web Servers     │  │  │ - Web Servers     │   │
│  │ - NAT Gateway     │  │  │ - NAT Gateway     │   │
│  └───────────────────┘  │  └───────────────────┘   │
│  ┌───────────────────┐  │  ┌───────────────────┐   │
│  │ Private Subnet    │  │  │ Private Subnet    │   │
│  │ 10.0.11.0/24      │  │  │ 10.0.12.0/24      │   │
│  │ - App Servers     │  │  │ - App Servers     │   │
│  └───────────────────┘  │  └───────────────────┘   │
│  ┌───────────────────┐  │  ┌───────────────────┐   │
│  │ Database Subnet   │  │  │ Database Subnet   │   │
│  │ 10.0.21.0/24      │  │  │ 10.0.22.0/24      │   │
│  │ - RDS             │  │  │ - RDS Standby     │   │
│  └───────────────────┘  │  └───────────────────┘   │
└─────────────────────────────────────────────────────┘
         │                              
    Internet Gateway                    
```

**Key Components:**

```yaml
1. Subnets:
   - Public: Has route to Internet Gateway
   - Private: No direct internet access
   
2. Route Tables:
   - Define traffic routing
   - Associated with subnets

3. Internet Gateway (IGW):
   - VPC connection to internet
   - One per VPC

4. NAT Gateway:
   - Allow private subnets to access internet
   - Placed in public subnet
   - Highly available in single AZ

5. Security Groups:
   - Stateful firewall
   - Instance level
   - Allow rules only

6. Network ACLs:
   - Stateless firewall
   - Subnet level
   - Allow and deny rules

7. VPC Peering:
   - Connect two VPCs
   - Private connectivity

8. VPC Endpoints:
   - Private connection to AWS services
   - Gateway endpoints: S3, DynamoDB
   - Interface endpoints: Most AWS services
```

---

## 🔐 IAM Advanced

### Q8: IAM Policies & Best Practices

**Answer:**

**Policy Types:**

```json
// Identity-based policy (attached to users/groups/roles)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}

// Resource-based policy (attached to resources like S3)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/Alice"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

**IAM Best Practices:**

1. ✅ Enable MFA for privileged users
2. ✅ Use roles instead of access keys
3. ✅ Apply least privilege principle
4. ✅ Use policy conditions for extra security
5. ✅ Rotate credentials regularly
6. ✅ Use CloudTrail for auditing
7. ✅ Create separate accounts for different environments

---

## 🏗️ CloudFormation

### Q9: Infrastructure as Code with CloudFormation

**Answer:**

```yaml
# CloudFormation Template
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Web Application Stack'

Parameters:
  KeyName:
    Description: EC2 Key Pair
    Type: AWS::EC2::KeyPair::KeyName
  
  InstanceType:
    Description: EC2 instance type
    Type: String
    Default: t3.micro
    AllowedValues:
      - t3.micro
      - t3.small
      - t3.medium

Resources:
  # VPC
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: MyVPC

  # Internet Gateway
  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: MyIGW

  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway

  # Public Subnet
  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: PublicSubnet

  # Security Group
  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow HTTP and SSH
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0

  # EC2 Instance
  WebServer:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0abcdef1234567890
      InstanceType: !Ref InstanceType
      KeyName: !Ref KeyName
      SubnetId: !Ref PublicSubnet
      SecurityGroupIds:
        - !Ref WebServerSecurityGroup
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          yum update -y
          yum install -y httpd
          systemctl start httpd
          systemctl enable httpd
          echo "<h1>Hello from CloudFormation</h1>" > /var/www/html/index.html
      Tags:
        - Key: Name
          Value: WebServer

Outputs:
  WebsiteURL:
    Description: URL of the website
    Value: !Sub 'http://${WebServer.PublicDnsName}'
  
  InstanceId:
    Description: Instance ID
    Value: !Ref WebServer
    Export:
      Name: !Sub '${AWS::StackName}-InstanceId'
```

---

## ⚡ Lambda & Serverless

### Q10: AWS Lambda

**Answer:**

**Lambda Features:**

```yaml
Triggers:
  - API Gateway
  - S3 events
  - DynamoDB Streams
  - CloudWatch Events
  - SNS/SQS
  - Application Load Balancer

Limits:
  Memory: 128 MB - 10 GB
  Timeout: 15 minutes max
  Deployment package: 50 MB (zipped), 250 MB (unzipped)
  /tmp storage: 512 MB - 10 GB
  Concurrent executions: 1000 (soft limit)

Pricing:
  - $0.20 per 1M requests
  - $0.0000166667 per GB-second
  - Free tier: 1M requests + 400,000 GB-seconds/month
```

**Lambda Function Example:**

```python
import json
import boto3

# Initialize AWS services
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    """
    Process S3 upload event and store metadata in DynamoDB
    """
    try:
        # Get S3 event details
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        size = event['Records'][0]['s3']['object']['size']
        
        # Get object metadata
        response = s3.head_object(Bucket=bucket, Key=key)
        
        # Store in DynamoDB
        table = dynamodb.Table('FileMetadata')
        table.put_item(
            Item={
                'fileKey': key,
                'bucket': bucket,
                'size': size,
                'contentType': response['ContentType'],
                'uploadTime': response['LastModified'].isoformat()
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully processed file')
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
```

---

## 🎯 Interview Questions

### Q11: Common AWS Interview Questions

**1. What is the difference between S3 and EBS?**

**Answer:**
- **S3:** Object storage, accessible via HTTP, unlimited storage, highly durable (99.999999999%)
- **EBS:** Block storage, attached to EC2, limited by volume size, for OS and databases

**2. Explain Multi-AZ vs Read Replicas in RDS**

**Answer:**
- **Multi-AZ:** Synchronous replication, automatic failover, same region, for high availability
- **Read Replicas:** Asynchronous replication, manual promotion, can be cross-region, for read scaling

**3. What is the difference between Security Groups and NACLs?**

**Answer:**
- **Security Groups:** Stateful, instance-level, allow rules only
- **NACLs:** Stateless, subnet-level, allow and deny rules

**4. How does Auto Scaling work?**

**Answer:**
- Monitors metrics (CPU, network, custom)
- Triggers scaling policies
- Launches/terminates instances based on demand
- Integrates with ELB for health checks

---

**Continue to Advanced AWS for production-ready architectures!** 🚀


---

## 💡 Simple Explanation (In Plain English)

Intermediate AWS connects pieces: **VPC** subnets and security groups for networking, **RDS** for managed SQL, **Lambda** for serverless functions, **ELB** for distributing traffic, and **CloudWatch** for metrics and alarms. You design **three-tier** apps (public load balancer, private app tier, private database) and use **IAM roles** so services talk securely without hard-coded keys.

---

## 🎯 Interview Quick Prep

### 1. What is a VPC and why does it matter?

**Simple Answer:** A Virtual Private Cloud is your isolated network in AWS. Subnets, route tables, and security groups control where resources live and which traffic is allowed.

### 2. RDS vs running MySQL on EC2?

**Simple Answer:** RDS is managed: backups, patching, Multi-AZ failover. EC2 gives full control but you operate everything. RDS is the default for production SQL unless you need exotic tuning.

### 3. When use Lambda?

**Simple Answer:** Lambda runs code on events without managing servers—good for APIs, webhooks, and light ETL. Pay per invocation and duration; cold starts and timeouts matter for design.

### 4. What does an Application Load Balancer do?

**Simple Answer:** ALB routes HTTP/HTTPS to healthy targets in multiple AZs, supports path/host routing, and integrates with Auto Scaling for elastic web tiers.

### 5. What is CloudWatch?

**Simple Answer:** CloudWatch collects metrics, logs, and alarms (e.g. high CPU triggers scale-out). It is the first place to debug production issues in AWS.
