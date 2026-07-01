import requests

url ="https://jsonplaceholder.tyicode.com/posts"

headers= {
    "content-type" : "application/json"
}

body= {
    "title" :" learning APIs",
    "body"  : "step 4 requests library",
    "userId": 1
}

response= requests.post(url, json=body, headers=headers)

print("status:", response.status_code)
print("created:", response.json())