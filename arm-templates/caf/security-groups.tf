resource "azuread_group" "administrator" {
  display_name = "Azure Administrators"
}

resource "azuread_group" "operator" {
  display_name = "Azure Operators"
}

resource "azuread_group" "security" {
  display_name = "Azure Security"
}

resource "azuread_group" "developer" {
  display_name = "Azure Developers"
}
