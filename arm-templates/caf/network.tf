resource "azurerm_resource_group" "vnet" {
  name     = "Network-RG"
  location = var.location
  tags     = var.tags
}

resource "azurerm_virtual_network" "hub" {
  name                = "CAF-Hub"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.vnet.location
  resource_group_name = azurerm_resource_group.vnet.name
}

resource "azurerm_subnet" "api-management" {
  name                 = "api-management"
  resource_group_name  = azurerm_resource_group.vnet.name
  virtual_network_name = azurerm_virtual_network.hub.name
  address_prefixes     = ["10.0.2.0/24"]
}

resource "azurerm_subnet" "app-gateway" {
  name                 = "app-gateway"
  resource_group_name  = azurerm_resource_group.vnet.name
  virtual_network_name = azurerm_virtual_network.hub.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_subnet" "app-service" {
  name                 = "app-service"
  resource_group_name  = azurerm_resource_group.vnet.name
  virtual_network_name = azurerm_virtual_network.hub.name
  address_prefixes     = ["10.0.5.0/24"]
  delegation {
    name = "delegation"
    service_delegation {
      name = "Microsoft.Web/serverFarms"
    }
  }
}

resource "azurerm_subnet" "container-instance" {
  name                 = "container-instance"
  resource_group_name  = azurerm_resource_group.vnet.name
  virtual_network_name = azurerm_virtual_network.hub.name
  address_prefixes     = ["10.0.3.0/24"]
  delegation {
    name = "delegation"
    service_delegation {
      name = "Microsoft.ContainerInstance/containerGroups"
    }
  }
}

resource "azurerm_subnet" "kubernetes" {
  name                 = "kubernetes"
  resource_group_name  = azurerm_resource_group.vnet.name
  virtual_network_name = azurerm_virtual_network.hub.name
  address_prefixes     = ["10.0.4.0/24"]
}
