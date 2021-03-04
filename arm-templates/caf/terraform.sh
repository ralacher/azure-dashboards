#!/bin/bash
mkdir -p /home/terraform
cp -r /mnt/azscripts/azscriptinput/* /home/terraform/

cd /home/terraform
unzip terraform_0.14.7_linux_amd64.zip -d /bin
sed -i 's|STORAGE_ACCOUNT_NAME|'"$STORAGE_ACCOUNT_NAME"'|g' main.tf
sed -i 's|SUBSCRIPTION_ID|'"$ARM_SUBSCRIPTION_ID"'|g' main.tf
sed -i 's|TENANT_ID|'"$ARM_TENANT_ID"'|g' main.tf

terraform init -input=false -no-color
terraform apply -input=false -no-color -auto-approve