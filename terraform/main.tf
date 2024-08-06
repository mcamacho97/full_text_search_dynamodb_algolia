# -------------------------------------------------
# SISTEMATICA BACKEND
# -------------------------------------------------
terraform {
  required_version = ">= 1.6.5"
  backend "s3" {
    bucket = "terraform-states-809489680864"
    key    = "full_text_search/workshop/terraform.tfstate"
    region = "us-east-1"
    # profile = "personal"
    encrypt = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
