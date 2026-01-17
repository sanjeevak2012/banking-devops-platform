variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
}

variable "public_subnet_cidrs" {
  description = "Public subnet CIDR blocks"
  type        = list(string)
}

variable "node_instance_type" {
  description = "EC2 instance type for EKS nodes"
  type        = string
}

variable "min_nodes" {
  description = "Minimum number of worker nodes"
  type        = number
}

variable "max_nodes" {
  description = "Maximum number of worker nodes"
  type        = number
}

variable "desired_nodes" {
  description = "Desired number of worker nodes"
  type        = number
}

variable "ecr_repository_name" {
  description = "ECR repository name"
  type        = string
}
