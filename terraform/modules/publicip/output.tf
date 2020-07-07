output "public_ip_address_id" {
  value = "${azurerm_public_ip.test.id}"
}

output "domain_name_label" {
  value = "${azurerm_public_ip.test.domain_name_label}"
}

output "public_ip_address" {
  value = "${azurerm_public_ip.test.ip_address}"
}