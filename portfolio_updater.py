import os
import json
import requests

def get_github_repos():
    token = os.environ["GITHUB_TOKEN_PORTFOLIO"]
    username = "jyothikashiju4-art"
    
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    repos = response.json()
    
    projects = []
    for repo in repos:
        if not repo["fork"]:  # skip forked repos
            projects.append({
                "name": repo["name"],
                "description": repo["description"] or "No description",
                "url": repo["html_url"],
                "language": repo["language"] or "Unknown",
                "stars": repo["stargazers_count"],
                "updated": repo["updated_at"][:10]
            })
    
    return projects

def save_json(projects):
    with open("projects.json", "w") as f:
        json.dump(projects, f, indent=2)
    print(f"✅ Saved {len(projects)} projects to projects.json")

def run():
    print("Fetching GitHub repos...")
    projects = get_github_repos()
    save_json(projects)
    
    for p in projects:
        print(f"- {p['name']} ({p['language']})")

if __name__ == "__main__":
    run()