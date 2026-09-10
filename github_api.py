import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

try:
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
except Exception:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


# =================================
# GET REPOSITORY
# =================================

def get_repository(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=headers
    )

    print("GitHub Status Code:", response.status_code)

    if response.status_code == 200:

        return response.json()

    else:

        print("GitHub Error:", response.text)

        return None


# =================================
# CHECK README
# =================================

def check_readme(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        return True

    return False


# =================================
# CHECK LICENSE
# =================================

def check_license(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        if data.get("license") is not None:

            return True

    return False


# =================================
# GET LAST UPDATED
# =================================

def get_last_updated(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        return data.get("updated_at")

    return None


# =================================
# GET TOPICS
# =================================

def get_topics(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/topics"

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        return data.get("names", [])

    return []


# =================================
# GET REPOSITORY SIZE
# =================================

def get_repository_size(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        # GitHub gives repository size in KB
        return data.get("size", 0)

    return 0


# =================================
# GET CONTRIBUTORS
# =================================

def get_contributors(owner, repo):

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/contributors?per_page=100"
    )

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        return len(data)

    return 0


# =================================
# GET RECENT COMMITS
# =================================

def get_recent_commits(owner, repo):

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/commits?per_page=100"
    )

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        return len(data)

    return 0


# =================================
# GET REPOSITORY FILES
# =================================

def get_repository_files(owner, repo):

    # First get repository information
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"

    repo_response = requests.get(
        repo_url,
        headers=headers
    )

    if repo_response.status_code != 200:

        return []

    repo_data = repo_response.json()

    # Get the default branch
    default_branch = repo_data.get(
        "default_branch",
        "main"
    )

    # Get repository tree
    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/git/trees/"
        f"{default_branch}?recursive=1"
    )

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        files = []

        for item in data.get("tree", []):

            if item.get("type") == "blob":

                files.append(
                    item.get("path")
                )

        return files

    return []


# =================================
# GET OPEN ISSUES
# =================================

def get_issues(owner, repo):

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/issues"
        f"?state=open&per_page=100"
    )

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        issues = []

        for item in data:

            # GitHub's issues API also returns pull requests
            if "pull_request" not in item:

                issues.append(item)

        return issues

    return []


# =================================
# GET OPEN PULL REQUESTS
# =================================

def get_pull_requests(owner, repo):

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/pulls"
        f"?state=open&per_page=100"
    )

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        return response.json()

    return []