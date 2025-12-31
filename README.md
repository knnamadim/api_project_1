# DevOps API Automation Project

## Overview

This project demonstrates how **APIs are used in real-world DevOps workflows** by integrating **GitHub** and **AWS** through automation.

The script:

1. Uses the **GitHub REST API** to retrieve the latest commit from a repository.
2. Uses the **AWS API (via Boto3)** to create an S3 bucket based on that commit.
3. Uploads a log file to S3 containing commit details.

This project showcases core DevOps skills:

* API fundamentals
* Automation with Python
* Cloud integration (AWS)
* Infrastructure interaction via code

---

## Architecture

```
GitHub API  --->  Python Automation Script  --->  AWS S3 API
     |                       |                     |
   Commits               Business Logic         Storage
```

---

## Technologies Used

* **Python 3.9+**
* **GitHub REST API**
* **AWS S3**
* **Boto3 (AWS SDK for Python)**
* **Requests (HTTP library)**

---

## Project Structure

```
devops_api_project/
│
├── main.py            # Main automation logic
├── config.py          # API credentials and configuration
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## Prerequisites

Before running this project, ensure you have:

1. **Python installed**

   ```bash
   python3 --version
   ```

2. **AWS Account**

   * Access Key ID
   * Secret Access Key
   * An S3-compatible region (e.g., us-east-1)

3. **GitHub Personal Access Token**

   * Required scopes: `repo`

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/devops_api_project.git
   cd devops_api_project
   ```

2. Create a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

Update `config.py` with your credentials:

```python
# GitHub settings
GITHUB_TOKEN = "your_github_personal_access_token"
GITHUB_USER = "your_github_username"

# AWS settings
AWS_ACCESS_KEY_ID = "your_aws_access_key_id"
AWS_SECRET_ACCESS_KEY = "your_aws_secret_access_key"
AWS_REGION = "us-east-1"
```

⚠️ **Security Note:** Never commit real credentials to GitHub. Use environment variables or `.gitignore` in production.

---

## How It Works

1. The script calls the **GitHub API** to fetch the latest commit from a repository.
2. If a commit is found:

   * A uniquely named **S3 bucket** is created using the commit SHA.
3. A log file containing commit details is uploaded to the bucket.

This simulates a DevOps automation workflow triggered by source code changes.

---

## Running the Project

Run the automation script:

```bash
python main.py
```

Expected output:

* Latest commit information printed to the console
* S3 bucket created
* Log file uploaded successfully

---

## Sample Output

```
Repo: example-repo
Latest commit: a1b2c3d4
Message: Initial commit
Bucket devops-log-a1b2c3 created successfully!
Log uploaded to devops-log-a1b2c3/log.txt
```

---

## DevOps Concepts Demonstrated

* REST APIs and HTTP methods
* Authentication using tokens
* Cloud automation using SDKs
* Infrastructure interaction via code
* Logging and auditing

---

## Possible Enhancements

* Run the script using **GitHub Actions** on every push
* Add **Slack or email notifications**
* Store logs in DynamoDB instead of S3
* Add unit tests and error handling
* Replace static credentials with **IAM Roles**

---

## Author

**Kimberly Nnamadim**
DevOps / Customer Success Engineer
