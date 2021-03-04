data "azurerm_client_config" "current" {}
data "azurerm_subscription" "current" {}

resource "azurerm_resource_group" "shared-service" {
  name     = "SharedService-RG"
  location = var.location
  tags     = var.tags
}

resource "azurerm_automation_account" "caf-automation" {
  name                = "CAF-${var.organization}-Automation-${random_integer.uniq.result}"
  location            = azurerm_resource_group.shared-service.location
  resource_group_name = azurerm_resource_group.shared-service.name
  sku_name            = "Basic"
  tags                = var.tags
}

resource "azurerm_key_vault" "caf-keyvault" {
  name                        = "CAF-${var.organization}-KeyVault-${random_integer.uniq.result}"
  location                    = azurerm_resource_group.shared-service.location
  resource_group_name         = azurerm_resource_group.shared-service.name
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false
  sku_name                    = "standard"
  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id
    secret_permissions = [
      "Get", "List", "Set", "Delete"
    ]
  }
}

resource "azurerm_log_analytics_workspace" "caf-loganalytics" {
  name                = "CAF-LogAnalytics-${random_integer.uniq.result}"
  location            = azurerm_resource_group.shared-service.location
  resource_group_name = azurerm_resource_group.shared-service.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_security_center_workspace" "example" {
  scope        = data.azurerm_subscription.current.id
  workspace_id = azurerm_log_analytics_workspace.caf-loganalytics.id
}
