data "aws_iam_policy_document" "sns_topic" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["s3.amazonaws.com"]
    }

    actions   = ["SNS:Publish"]
    resources = ["arn:aws:sns:*:*:${var.sns_topic_name}"]
  }
}
data "aws_iam_policy_document" "sns_topic" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["s3.amazonaws.com"]
    }

    actions   = ["SNS:Publish"]
    resources = ["arn:aws:sns:*:*:${var.sns_topic_name}"]
  }
}

resource "aws_sns_topic" "topic" {
  name   = var.sns_topic_name
  policy = data.aws_iam_policy_document.sns_topic.json
  tags   = var.project_tags
}