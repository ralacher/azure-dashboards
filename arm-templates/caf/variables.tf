variable "location" {
  type    = string
  default = "eastus2"
}

variable "tags" {
  default = {
    CostCenter = "P-1234"
  }
}

variable "organization" {
  type = string
}
