resource "aws_ecr_repository" "ecr_repository" {
  name = var.ecr_repository_name
  tags = var.project_tags
}

resource "null_resource" "docker_build_and_push" {
  triggers = {
    always_run = "${timestamp()}"
  }

  provisioner "local-exec" {
    command = <<-EOL
      set -e
      cd ../
      sudo chmod 666 /var/run/docker.sock
      sudo aws ecr get-login-password --region ${var.aws_region} | docker login --username AWS --password-stdin ${var.aws_account_name}.dkr.ecr.${var.aws_region}.amazonaws.com
      echo "BUILDING"
      docker build -t ${var.ecr_repository_name} .
      echo "TAGGING"
      docker tag ${var.ecr_repository_name}:latest ${var.aws_account_name}.dkr.ecr.${var.aws_region}.amazonaws.com/${var.ecr_repository_name}:latest
      echo "PUSHING"
      docker push ${var.aws_account_name}.dkr.ecr.${var.aws_region}.amazonaws.com/${var.ecr_repository_name}:latest
    EOL
  }
}

resource "aws_iam_role" "aws_ecr_role" {
  name = var.aws_ecr_role_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })

  inline_policy {
    name = var.aws_ecr_policy_name
    policy = jsonencode({
      Version = "2012-10-17",
      Statement = [
        {
          Action = [
            "secretsmanager:GetSecretValue",
            "s3:PutObject",
            "s3:GetObject",
            "ecr:*",
            "logs:CreateLogStream",
            "logs:DescribeLogGroups",
            "logs:DescribeLogStreams",
            "logs:GetLogEvents",
            "logs:CreateLogGroup",
            "logs:PutLogEvents",
            "sns:*"
          ],
          Effect = "Allow",
          Resource = "*"
        }
      ]
    })
  }
  
}

resource "aws_cloudwatch_log_group" "ecr_cloudwatch_log_group" {
  name = var.aws_ecr_cloudwatch_log_group_name

  retention_in_days = 14

  tags = var.project_tags
}

resource "aws_ecs_cluster" "ecs_cluster" {
  name = var.aws_ecs_cluster_name
  tags = var.project_tags
}

resource "aws_ecs_task_definition" "ecs_task_definition" {
  family                   = var.ecs_task_definition_name
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "2048"
  execution_role_arn       = aws_iam_role.aws_ecr_role.arn
  task_role_arn            = aws_iam_role.aws_ecr_role.arn

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }


  container_definitions = jsonencode([{
    name  = "${var.ecr_repository_name}-container"
    image = "${aws_ecr_repository.ecr_repository.repository_url}"
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        awslogs-group         = var.aws_ecr_cloudwatch_log_group_name
        awslogs-region        = var.aws_region
        awslogs-stream-prefix = "challenge"
      }
    }
    essential = true
    memory          = 2048
    cpu             = 256 
    portMappings = [
      {
        containerPort = 8080
        hostPort      = 8080
        protocol      = "tcp"
      },
      {
        containerPort = 443
        hostPort      = 443
        protocol      = "tcp"
      }
    ]
  }])
  tags = var.project_tags
}
