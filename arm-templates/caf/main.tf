terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.49.0"
    }
    azuread = {
      source  = "hashicorp/azuread"
      version = "=1.4.0"
    }
  }
}

provider "azuread" {
}
provider "azurerm" {
  features {}
}
