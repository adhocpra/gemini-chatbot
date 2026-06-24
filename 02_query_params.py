#api filter results using key=values in the url so pass a dict:

import requests

response= requests.get("https://api.github.com/search/repositories",
params= {"q":"fastapi","sort":"stars", "per_page":3})

data= response.json()
for repo in data["items"]:
    print(repo["full_name"], "-", repo ["stargazers_count"], "stars")