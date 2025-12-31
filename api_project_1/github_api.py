# github_api.py

import requests
from config import GITHUB_TOKEN, GITHUB_USERNAME

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_latest_commit(repo_name):
    """
    Fetch the latest commit SHA and message for a given repo
    """
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/commits"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch commits: {response.text}")

    commit_data = response.json()[0]
    return {
        "sha": commit_data["sha"],
        "message": commit_data["commit"]["message"]
    }
