import requests


url= "https://api.github.com//users/adhocpra"

response= requests.get(url)
print("status code:" , response.status_code)
print("Response JSON:", response.json())