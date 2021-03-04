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
    random = {
      source = "hashicorp/random"
      version = "=3.1.0"
    }
  }
  backend "azurerm" {
    resource_group_name   = "Identity-RG"
    storage_account_name  = "STORAGE_ACCOUNT_NAME"
    container_name        = "tfstate"
    key                   = "foundation.tfstate"
  }
}

provider "azurerm" {
  features {}
}
provider "azuread" {}
provider "random" {}

resource "random_integer" "uniq" {
  min = 10
  max = 99
}
