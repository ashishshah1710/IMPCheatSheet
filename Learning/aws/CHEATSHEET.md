# ☁️ AWS CLI Cheat Sheet

## AWS CLI Configuration

```bash
# Configure AWS CLI
aws configure

# Configure with profile
aws configure --profile production

# List configured profiles
aws configure list-profiles

# Use specific profile
aws s3 ls --profile production

# Set default profile
export AWS_PROFILE=production

# View configuration
aws configure list
aws configure get region

# Get caller identity
aws sts get-caller-identity
```

## IAM (Identity and Access Management)

```bash
# Users
aws iam list-users
aws iam create-user --user-name john
aws iam delete-user --user-name john
aws iam get-user --user-name john

# Access keys
aws iam create-access-key --user-name john
aws iam list-access-keys --user-name john
aws iam delete-access-key --user-name john --access-key-id AKIAXXXXX

# Groups
aws iam list-groups
aws iam create-group --group-name developers
aws iam delete-group --group-name developers
aws iam add-user-to-group --user-name john --group-name developers

# Policies
aws iam list-policies
aws iam list-attached-user-policies --user-name john
aws iam attach-user-policy --user-name john --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess
aws iam detach-user-policy --user-name john --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess

# Roles
aws iam list-roles
aws iam create-role --role-name lambda-role --assume-role-policy-document file://trust-policy.json
aws iam attach-role-policy --role-name lambda-role --policy-arn arn:aws:iam::aws:policy/AWSLambdaExecute

# Account info
aws sts get-caller-identity
aws iam get-account-summary
```

## EC2 (Elastic Compute Cloud)

```bash
# Instances
aws ec2 describe-instances
aws ec2 describe-instances --instance-ids i-1234567890abcdef0
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"

# Start/Stop instances
aws ec2 start-instances --instance-ids i-1234567890abcdef0
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
aws ec2 reboot-instances --instance-ids i-1234567890abcdef0
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0

# Launch instance
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name my-key \
  --security-group-ids sg-12345678 \
  --subnet-id subnet-12345678

# Instance info
aws ec2 describe-instance-status --instance-ids i-1234567890abcdef0
aws ec2 get-console-output --instance-id i-1234567890abcdef0

# AMIs
aws ec2 describe-images --owners self
aws ec2 describe-images --image-ids ami-12345678
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "My-Image"
aws ec2 deregister-image --image-id ami-12345678

# Key pairs
aws ec2 describe-key-pairs
aws ec2 create-key-pair --key-name my-key --query 'KeyMaterial' --output text > my-key.pem
aws ec2 delete-key-pair --key-name my-key

# Security groups
aws ec2 describe-security-groups
aws ec2 create-security-group --group-name web-sg --description "Web servers"
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
aws ec2 delete-security-group --group-id sg-12345678

# Elastic IPs
aws ec2 allocate-address
aws ec2 describe-addresses
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345678
aws ec2 release-address --allocation-id eipalloc-12345678

# Snapshots
aws ec2 describe-snapshots --owner-ids self
aws ec2 create-snapshot --volume-id vol-12345678 --description "Backup"
aws ec2 delete-snapshot --snapshot-id snap-12345678

# Volumes
aws ec2 describe-volumes
aws ec2 create-volume --availability-zone us-east-1a --size 10
aws ec2 attach-volume --volume-id vol-12345678 --instance-id i-1234567890abcdef0 --device /dev/sdf
aws ec2 detach-volume --volume-id vol-12345678
aws ec2 delete-volume --volume-id vol-12345678
```

## S3 (Simple Storage Service)

```bash
# Buckets
aws s3 ls
aws s3 mb s3://my-bucket-name
aws s3 rb s3://my-bucket-name
aws s3 rb s3://my-bucket-name --force  # Delete non-empty bucket

# Objects
aws s3 ls s3://my-bucket/
aws s3 ls s3://my-bucket/folder/ --recursive
aws s3 cp file.txt s3://my-bucket/
aws s3 cp s3://my-bucket/file.txt ./
aws s3 cp s3://bucket1/file.txt s3://bucket2/  # Copy between buckets
aws s3 rm s3://my-bucket/file.txt
aws s3 rm s3://my-bucket/folder/ --recursive

# Sync
aws s3 sync ./local-folder s3://my-bucket/
aws s3 sync s3://my-bucket/ ./local-folder
aws s3 sync s3://bucket1/ s3://bucket2/

# Presigned URLs
aws s3 presign s3://my-bucket/file.txt --expires-in 3600

# Bucket operations
aws s3api list-buckets
aws s3api create-bucket --bucket my-bucket --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
aws s3api delete-bucket --bucket my-bucket

# Bucket policy
aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
aws s3api get-bucket-policy --bucket my-bucket
aws s3api delete-bucket-policy --bucket my-bucket

# Versioning
aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled
aws s3api get-bucket-versioning --bucket my-bucket

# Website hosting
aws s3 website s3://my-bucket/ --index-document index.html --error-document error.html

# ACL
aws s3api put-object-acl --bucket my-bucket --key file.txt --acl public-read

# List object versions
aws s3api list-object-versions --bucket my-bucket
```

## VPC (Virtual Private Cloud)

```bash
# VPCs
aws ec2 describe-vpcs
aws ec2 create-vpc --cidr-block 10.0.0.0/16
aws ec2 delete-vpc --vpc-id vpc-12345678

# Subnets
aws ec2 describe-subnets
aws ec2 create-subnet --vpc-id vpc-12345678 --cidr-block 10.0.1.0/24
aws ec2 delete-subnet --subnet-id subnet-12345678

# Internet Gateways
aws ec2 describe-internet-gateways
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway --internet-gateway-id igw-12345678 --vpc-id vpc-12345678
aws ec2 detach-internet-gateway --internet-gateway-id igw-12345678 --vpc-id vpc-12345678
aws ec2 delete-internet-gateway --internet-gateway-id igw-12345678

# Route Tables
aws ec2 describe-route-tables
aws ec2 create-route-table --vpc-id vpc-12345678
aws ec2 create-route --route-table-id rtb-12345678 --destination-cidr-block 0.0.0.0/0 --gateway-id igw-12345678
aws ec2 associate-route-table --route-table-id rtb-12345678 --subnet-id subnet-12345678

# NAT Gateways
aws ec2 describe-nat-gateways
aws ec2 create-nat-gateway --subnet-id subnet-12345678 --allocation-id eipalloc-12345678
aws ec2 delete-nat-gateway --nat-gateway-id nat-12345678

# Network ACLs
aws ec2 describe-network-acls
```

## RDS (Relational Database Service)

```bash
# DB Instances
aws rds describe-db-instances
aws rds describe-db-instances --db-instance-identifier mydb

# Create DB instance
aws rds create-db-instance \
  --db-instance-identifier mydb \
  --db-instance-class db.t2.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password password123 \
  --allocated-storage 20

# Delete DB instance
aws rds delete-db-instance --db-instance-identifier mydb --skip-final-snapshot

# Start/Stop
aws rds start-db-instance --db-instance-identifier mydb
aws rds stop-db-instance --db-instance-identifier mydb

# Snapshots
aws rds describe-db-snapshots
aws rds create-db-snapshot --db-instance-identifier mydb --db-snapshot-identifier mydb-snapshot
aws rds delete-db-snapshot --db-snapshot-identifier mydb-snapshot

# Restore from snapshot
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier mydb-restored \
  --db-snapshot-identifier mydb-snapshot
```

## Lambda

```bash
# List functions
aws lambda list-functions

# Get function
aws lambda get-function --function-name my-function

# Create function
aws lambda create-function \
  --function-name my-function \
  --runtime python3.9 \
  --role arn:aws:iam::123456789012:role/lambda-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip

# Update function code
aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip

# Update function configuration
aws lambda update-function-configuration \
  --function-name my-function \
  --timeout 30 \
  --memory-size 512

# Invoke function
aws lambda invoke --function-name my-function output.txt
aws lambda invoke --function-name my-function --payload '{"key":"value"}' output.txt

# Delete function
aws lambda delete-function --function-name my-function

# List versions
aws lambda list-versions-by-function --function-name my-function

# List aliases
aws lambda list-aliases --function-name my-function
```

## ECS (Elastic Container Service)

```bash
# Clusters
aws ecs list-clusters
aws ecs describe-clusters --clusters my-cluster
aws ecs create-cluster --cluster-name my-cluster
aws ecs delete-cluster --cluster my-cluster

# Task Definitions
aws ecs list-task-definitions
aws ecs describe-task-definition --task-definition my-task:1
aws ecs register-task-definition --cli-input-json file://task-definition.json
aws ecs deregister-task-definition --task-definition my-task:1

# Services
aws ecs list-services --cluster my-cluster
aws ecs describe-services --cluster my-cluster --services my-service
aws ecs create-service --cluster my-cluster --service-name my-service --task-definition my-task --desired-count 2
aws ecs update-service --cluster my-cluster --service my-service --desired-count 3
aws ecs delete-service --cluster my-cluster --service my-service

# Tasks
aws ecs list-tasks --cluster my-cluster
aws ecs describe-tasks --cluster my-cluster --tasks task-id
aws ecs run-task --cluster my-cluster --task-definition my-task
aws ecs stop-task --cluster my-cluster --task task-id
```

## EKS (Elastic Kubernetes Service)

```bash
# Clusters
aws eks list-clusters
aws eks describe-cluster --name my-cluster
aws eks create-cluster --name my-cluster --role-arn arn:aws:iam::123456789012:role/eks-role --resources-vpc-config subnetIds=subnet-12345,subnet-67890
aws eks delete-cluster --name my-cluster

# Update kubeconfig
aws eks update-kubeconfig --name my-cluster

# Node groups
aws eks list-nodegroups --cluster-name my-cluster
aws eks describe-nodegroup --cluster-name my-cluster --nodegroup-name my-nodes
aws eks create-nodegroup --cluster-name my-cluster --nodegroup-name my-nodes --subnets subnet-12345 --instance-types t3.medium --node-role arn:aws:iam::123456789012:role/node-role
```

## ECR (Elastic Container Registry)

```bash
# Repositories
aws ecr describe-repositories
aws ecr create-repository --repository-name my-app
aws ecr delete-repository --repository-name my-app --force

# Images
aws ecr list-images --repository-name my-app
aws ecr describe-images --repository-name my-app
aws ecr batch-delete-image --repository-name my-app --image-ids imageTag=latest

# Login
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com

# Push image
docker tag my-app:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest

# Pull image
docker pull 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
```

## CloudFormation

```bash
# Stacks
aws cloudformation list-stacks
aws cloudformation describe-stacks --stack-name my-stack
aws cloudformation create-stack --stack-name my-stack --template-body file://template.yaml
aws cloudformation update-stack --stack-name my-stack --template-body file://template.yaml
aws cloudformation delete-stack --stack-name my-stack

# Stack events
aws cloudformation describe-stack-events --stack-name my-stack

# Stack resources
aws cloudformation describe-stack-resources --stack-name my-stack

# Validate template
aws cloudformation validate-template --template-body file://template.yaml

# Change sets
aws cloudformation create-change-set --stack-name my-stack --change-set-name my-changes --template-body file://template.yaml
aws cloudformation describe-change-set --stack-name my-stack --change-set-name my-changes
aws cloudformation execute-change-set --stack-name my-stack --change-set-name my-changes
```

## CloudWatch

```bash
# Logs
aws logs describe-log-groups
aws logs describe-log-streams --log-group-name /aws/lambda/my-function
aws logs filter-log-events --log-group-name /aws/lambda/my-function --filter-pattern ERROR
aws logs tail /aws/lambda/my-function --follow

# Metrics
aws cloudwatch list-metrics
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --start-time 2023-01-01T00:00:00Z \
  --end-time 2023-01-02T00:00:00Z \
  --period 3600 \
  --statistics Average

# Alarms
aws cloudwatch describe-alarms
aws cloudwatch put-metric-alarm \
  --alarm-name high-cpu \
  --alarm-description "High CPU usage" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --evaluation-periods 2 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold
aws cloudwatch delete-alarms --alarm-names high-cpu
```

## Route 53 (DNS)

```bash
# Hosted zones
aws route53 list-hosted-zones
aws route53 create-hosted-zone --name example.com --caller-reference $(date +%s)

# Record sets
aws route53 list-resource-record-sets --hosted-zone-id Z123456789ABC

# Change record sets
aws route53 change-resource-record-sets --hosted-zone-id Z123456789ABC --change-batch file://changes.json
```

## ElastiCache

```bash
# Redis clusters
aws elasticache describe-cache-clusters
aws elasticache create-cache-cluster \
  --cache-cluster-id my-redis \
  --cache-node-type cache.t2.micro \
  --engine redis \
  --num-cache-nodes 1
aws elasticache delete-cache-cluster --cache-cluster-id my-redis
```

## DynamoDB

```bash
# Tables
aws dynamodb list-tables
aws dynamodb describe-table --table-name my-table
aws dynamodb create-table \
  --table-name my-table \
  --attribute-definitions AttributeName=id,AttributeType=S \
  --key-schema AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
aws dynamodb delete-table --table-name my-table

# Items
aws dynamodb put-item --table-name my-table --item '{"id":{"S":"1"},"name":{"S":"John"}}'
aws dynamodb get-item --table-name my-table --key '{"id":{"S":"1"}}'
aws dynamodb scan --table-name my-table
aws dynamodb query --table-name my-table --key-condition-expression "id = :id" --expression-attribute-values '{":id":{"S":"1"}}'
aws dynamodb delete-item --table-name my-table --key '{"id":{"S":"1"}}'
```

## SNS (Simple Notification Service)

```bash
# Topics
aws sns list-topics
aws sns create-topic --name my-topic
aws sns delete-topic --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic

# Subscriptions
aws sns subscribe --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic --protocol email --notification-endpoint my-email@example.com
aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic

# Publish
aws sns publish --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic --message "Hello from SNS"
```

## SQS (Simple Queue Service)

```bash
# Queues
aws sqs list-queues
aws sqs create-queue --queue-name my-queue
aws sqs get-queue-url --queue-name my-queue
aws sqs delete-queue --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue

# Messages
aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue --message-body "Hello"
aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue
aws sqs delete-message --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue --receipt-handle RECEIPT_HANDLE
```

## Useful Filters and Queries

```bash
# Filter EC2 instances
aws ec2 describe-instances --filters "Name=tag:Name,Values=WebServer"
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"

# Query specific fields
aws ec2 describe-instances --query 'Reservations[].Instances[].InstanceId'
aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,State.Name,PublicIpAddress]' --output table

# Get all running instance IDs
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query 'Reservations[].Instances[].InstanceId' --output text

# Get S3 bucket sizes
aws s3 ls --summarize --human-readable --recursive s3://my-bucket

# List all resources with specific tag
aws resourcegroupstaggingapi get-resources --tag-filters Key=Environment,Values=Production
```

## Output Formats

```bash
# JSON (default)
aws s3 ls --output json

# Table
aws ec2 describe-instances --output table

# Text
aws ec2 describe-instances --output text

# YAML
aws cloudformation describe-stacks --output yaml
```

## Common Patterns

```bash
# Stop all running EC2 instances
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query 'Reservations[].Instances[].InstanceId' --output text | xargs aws ec2 stop-instances --instance-ids

# List all resources in region
aws resourcegroupstaggingapi get-resources --region us-east-1

# Get account ID
aws sts get-caller-identity --query Account --output text

# List all regions
aws ec2 describe-regions --query 'Regions[].RegionName' --output text

# Check service quotas
aws service-quotas list-service-quotas --service-code ec2
```

## Aliases

```bash
# Add to ~/.bashrc or ~/.zshrc

alias awswho='aws sts get-caller-identity'
alias awsregion='aws configure get region'
alias ec2list='aws ec2 describe-instances --query "Reservations[].Instances[].[InstanceId,State.Name,PublicIpAddress,Tags[?Key==\`Name\`].Value|[0]]" --output table'
alias s3list='aws s3 ls'
alias lambdalist='aws lambda list-functions --query "Functions[].[FunctionName,Runtime,LastModified]" --output table'
```

## Best Practices

```bash
# Always specify region
aws ec2 describe-instances --region us-east-1

# Use profiles for different accounts
aws s3 ls --profile production

# Use pagination for large results
aws s3api list-objects-v2 --bucket my-bucket --max-items 100

# Use --dry-run to test commands
aws ec2 run-instances --dry-run --image-id ami-12345678 --instance-type t2.micro

# Enable CLI auto-completion
complete -C aws_completer aws
```

---

**Pro Tip:** Use `--query` with JMESPath to filter and format output!

```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name]' --output text
```

