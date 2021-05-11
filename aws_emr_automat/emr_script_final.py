import boto3
import subprocess

s3_client = boto3.resource('s3')
BUCKET = "EXISTING_S3_BUCKET"

s3_client.Bucket(BUCKET).upload_file("FULLPATH/to/sample.json", "sampl.json")
s3_client.Bucket(BUCKET).upload_file("FULLPATH/to/spark_job.py", "sparkjob.py")

subprocess.Popen(["python", "FULLPATH/to/copytos3mail.py"])

subprocess.Popen(["python", "FULLPATH/to/emr_script.py"])