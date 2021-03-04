resource "azurerm_resource_group" "web" {
  name     = "Web-RG"
  location = var.location
  tags     = var.tags
}
