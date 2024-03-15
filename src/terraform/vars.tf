variable "aws_region" {
  description = "The AWS region to deploy resources into"
  default = "us-east-1"
}

variable "terraform_bucket_name" {
  description = "The name of the S3 bucket used for storing Terraform state files"
  default = "bucket-name"
}

variable "terraform_bucket_key" {
  description = "The S3 bucket key under which to store the Terraform state file"
  default = "bucket_path/key.tfstate"
}

variable "dynamodb_lock_table" {
  description = "The name of the DynamoDB table used for state locking and consistency checking"
  default = "dynamodb-lock-table"
}

variable "project_tags" {
  description = "Common tags to be applied to all resources"
  type        = map(string)
  default     = {
    Project = "DefaultProject"
    Owner   = "DefaultOwner"
  }
}

variable "vpc_id" {
  description = "The ID of the VPC where resources will be deployed"
  type        = string
  default     = "vpc-123abc"
}

variable "security_group_ids" {
  description = "A list of security group IDs to be associated with resources"
  type        = list(string)
  default     = ["sg-123abc", "sg-456def"]
}

variable "subnet_ids" {
  description = "A list of subnet IDs where resources will be deployed"
  type        = list(string)
  default     = ["subnet-123abc", "subnet-456def", "subnet-789ghi"]
}

variable "sns_topic_name" {
  description = "The name of the SNS topic"
  type        = string
  default     = "default-sns-topic-name"
}

variable "ecr_repository_name" {
  description = "The name of the ECR repository"
  type        = string
  default     = "challenge-de-latam-repository"
}

variable "aws_account_name" {
  description = "The value of the AWS account"
  type        = string
  default     = "123456789012"
}

variable "aws_ecr_role_name" {
  description = "The name of the ECR role"
  type        = string
  default     = "aws-ecr-role-name"
}

variable "aws_ecr_policy_name" {
  description = "The name of the ECR role"
  type        = string
  default     = "aws-ecr-policy-name"
}

variable "aws_ecr_cloudwatch_log_group_name" {
  description = "The name of the ECR Cloudwatch log group"
  type        = string
  default     = "ecr-cloudwatch-log-group"
}

variable "aws_ecs_cluster_name" {
  description = "The name of the ECS cluster name"
  type        = string
  default     = "ecs-cluster-name"
}

variable "ecs_task_definition_name" {
  description = "The name of the ECS task definition"
  type        = string
  default     = "ecs-task-definition"
}

