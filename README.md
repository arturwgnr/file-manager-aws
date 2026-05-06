# File Upload & Storage Manager 

A production-minded file management web application backed by AWS S3.

## Stack
- Python / Flask
- AWS S3 (boto3)
- AWS EC2
- IAM Role (no hardcoded credentials)

## Features
- Upload files to a private S3 bucket
- List all stored files with upload date
- Delete files from the bucket

## Architecture
- Flask running on EC2 (eu-west-1)
- IAM Role attached to EC2 for S3 access via Instance Metadata Service (IMDS)
- No AWS credentials stored in code

## Author
Artur Wagner · Cloud Engineer
