# main.py

from github_api import get_latest_commit
from aws_s3 import create_bucket, upload_log

REPO_NAME = "example-repo"  # replace with one of your repos

def main():
    print("🔍 Checking GitHub for latest commit...")

    commit = get_latest_commit(REPO_NAME)
    short_sha = commit["sha"][:6]

    bucket_name = f"devops-api-log-{short_sha}"

    print("☁️ Creating S3 bucket...")
    create_bucket(bucket_name)

    log_content = (
        f"Repository: {REPO_NAME}\n"
        f"Commit SHA: {commit['sha']}\n"
        f"Message: {commit['message']}\n"
    )

    print("⬆️ Uploading log to S3...")
    upload_log(bucket_name, log_content)

    print("🎉 Automation completed successfully!")

if __name__ == "__main__":
    main()
