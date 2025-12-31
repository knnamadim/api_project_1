# aws_s3.py

import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

def create_bucket(bucket_name):
    s3 = get_s3_client()

    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": AWS_REGION
            }
        )
        print(f"✅ S3 bucket created: {bucket_name}")
    except Exception as e:
        print(f"❌ Bucket creation failed: {e}")

def upload_log(bucket_name, content, filename="commit_log.txt"):
    s3 = get_s3_client()

    s3.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=content
    )

    print(f"📄 Log uploaded to s3://{bucket_name}/{filename}")
