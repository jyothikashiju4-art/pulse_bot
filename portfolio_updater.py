import os
import json
import requests

def get_github_repos():
    token = os.environ["TOKEN_GITHUB"]
    username = "jyothikashiju4-art"
    
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    data = response.json()
    
    # Check if API returned an error
    if isinstance(data, dict) and "message" in data:
        print(f"API Error: {data['message']}")
        return []
    
    projects = []
    for repo in data:
        if not repo["fork"]:
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
