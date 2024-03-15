provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket = var.terraform_bucket_name
    key    = var.terraform_bucket_key
    region         = var.aws_region
    encrypt        = true
    dynamodb_table = var.dynamodb_lock_table
  }
}
