import requests

response= requests.get("https://api.github.com/users/thisuserdoesnotexist999")
if response.status_code ==200:
    print(response.json())
elif response.status_code==404:
    print("User not found")
else:
    response.raise_for_status()