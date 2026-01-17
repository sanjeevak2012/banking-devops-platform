aws_region = "ap-south-1"

cluster_name = "banking-eks"

vpc_cidr = "10.0.0.0/16"

public_subnet_cidrs = [
  "10.0.1.0/24",
  "10.0.2.0/24"
]

node_instance_type = "t3.medium"

min_nodes     = 1
desired_nodes = 2
max_nodes     = 3

ecr_repository_name = "banking-transaction-service"
