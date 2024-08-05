    # Repository Python Github :
    # Request Libary :
        
import requests

def get_repositories(language, num_repos=5):
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc'
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()['items'][:num_repos]
        for i, repo in enumerate(repositories, 1):
            print(f"{i}. {repo['name']} by {repo['owner']['login']}")
            print(f"   URL: {repo['html_url']}")
            print(f"   Description: {repo['description']}\n")
    else:
        print("Failed to retrieve data from GitHub API")

if __name__ == "main":
    language = input("Please enter the programming language: ")
    get_repositories(language)
