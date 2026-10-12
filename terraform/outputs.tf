output "network_name" {
  description = "Name of the Terraform-managed Docker network"
  value       = docker_network.devops.name
}

output "network_id" {
  description = "ID of the Terraform-managed Docker network"
  value       = docker_network.devops.id
}
