# API / HTTP / Requests — Quick Reference

## What is an API?
A set of rules that lets two programs talk to each other.
- **Client** — the one asking (your code, browser, app)
- **Server** — the one answering (GitHub, Gemini, etc.)
- **API** — the middleman with fixed rules for communication

Flow: `Client → REQUEST → Server → RESPONSE → Client`

---

## HTTP Methods

| Method | What it does | When you use it |
|--------|-------------|-----------------|
| `GET` | Fetch / read data | Getting a GitHub profile |
| `POST` | Send new data / create | Sending a message to Gemini |
| `PUT` | Replace / update existing data | Editing a resource |
| `DELETE` | Remove something | Deleting a resource |

---

## Status Codes

| Code | Meaning | Who's at fault |
|------|---------|----------------|
| `200` | OK — success | — |
| `201` | Created — new resource made | — |
| `400` | Bad Request — malformed data | You |
| `401` | Unauthorized — missing/wrong API key | You |
| `403` | Forbidden — no permission | You |
| `404` | Not Found — URL doesn't exist | You |
| `429` | Too Many Requests — rate limit hit | You (slow down) |
| `500` | Internal Server Error — server crashed | Them |

---

## Request Structure

```
METHOD  https://api.example.com/endpoint
Headers:
  Content-Type: application/json
  Authorization: Bearer YOUR_API_KEY

Body (POST only):
  {
    "key": "value"
  }
```

---

## JSON

The data format APIs use — looks like a Python dict:

```json
{
  "name": "Pravat",
  "age": 20,
  "skills": ["Python", "FastAPI"],
  "active": true
}
```

---

## Python `requests` Cheatsheet

```python
import requests

# GET
response = requests.get("https://api.example.com/data")

# GET with query params (?q=python&sort=stars)
response = requests.get(url, params={"q": "python", "sort": "stars"})

# POST with JSON body
response = requests.post(url, json={"message": "hello"}, headers={"Authorization": "Bearer KEY"})

# Read the response
response.status_code     # 200, 404, etc.
response.json()          # parse body as Python dict

# Crash loudly if request failed (4xx / 5xx)
response.raise_for_status()
```

---

## Key Concepts

| Concept | What it is |
|---------|-----------|
| Headers | Metadata on a request (auth, content type) |
| Body | Data you send with POST/PUT |
| Query params | Filters in the URL after `?` |
| JSON | Text format for sending structured data |
| `.raise_for_status()` | Auto-raises exception on bad status codes |
| `params={}` | requests builds the `?key=value` URL for you |
| `json={}` | Auto-serializes dict + sets Content-Type header |
