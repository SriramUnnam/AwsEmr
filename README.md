# AwsEmr
EMR Cluster spin up automation Python boto3

## awscli
The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts. As a prerequisite awscli must configured in the local system, refer to the documentation on how to configure awscli, https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

## boto3
Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts.

## Installation
Use the package manager [pip] to install boto3
```bash
pip install boto3
```

## Usage

```python
import boto3

s3_client = boto3.resource('s3')
BUCKET = "EXISTING_S3_BUCKET"

s3_client.Bucket(BUCKET).upload_file("FULLPATH/to/sample.json", "sampl.json")
```
