resource "aws_vpc_endpoint" "sns" {
  vpc_id = var.vpc_id
  service_name = "com.amazonaws.us-east-1.sns"
  vpc_endpoint_type  = "Interface"
  security_group_ids = var.security_group_ids
  subnet_ids         = var.subnet_ids
  private_dns_enabled = true
}

resource "aws_vpc_endpoint" "ecs" {
  vpc_id = var.vpc_id
  service_name = "com.amazonaws.us-east-1.ecs"
  vpc_endpoint_type  = "Interface"
  security_group_ids = var.security_group_ids
  subnet_ids         = var.subnet_ids
  private_dns_enabled = true
}

resource "aws_vpc_endpoint" "s3" {
  vpc_id = var.vpc_id
  service_name = "com.amazonaws.us-east-1.s3"
  vpc_endpoint_type  = "Gateway"
}