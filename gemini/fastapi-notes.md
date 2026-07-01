# FastAPI / REST API — Complete Reference

## What is FastAPI?
A Python framework for building APIs — you write Python functions and FastAPI turns them into HTTP endpoints anyone can call.

- You were the **client** calling Gemini's API
- Now you are building the **server**

---

## What is REST API?

| Rule | Meaning |
|------|---------|
| Use HTTP methods correctly | GET=read, POST=create, DELETE=remove |
| URLs are nouns not verbs | `/chat` not `/sendMessage` |
| Communicate with JSON | Request and response bodies are JSON |
| Stateless | Each request carries everything the server needs |

---

## What is uvicorn?

FastAPI needs a server to listen for requests. Uvicorn is that server.

```
uvicorn = the engine
FastAPI = the steering wheel and controls
```

Always start your app with:
```bash
python3 -m uvicorn main:app --reload
```

| Part | Meaning |
|------|---------|
| `main` | Your filename (main.py) |
| `app` | The variable name inside it (app = FastAPI()) |
| `--reload` | Auto-restarts when you save changes |

---

## What is a decorator?

A line starting with `@` that wraps the function below it and adds extra behaviour.

```python
@app.get("/")       # decorator: "register this as a GET route at /"
def root():         # your function
    return {...}    # what gets sent back as JSON
```

FastAPI reads the decorator and says: whenever a GET request comes to `/`, call `root()`

---

## What is Pydantic?

Defines the shape of your data using Python classes. FastAPI uses it to:
- Parse the JSON body automatically
- Validate it (reject if fields are missing or wrong type)
- Convert it into a Python object you can use

```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str        # must be a string
```

No manual validation needed — FastAPI handles it automatically.

---

## Route Types

| Decorator | HTTP Method | Use for |
|-----------|------------|---------|
| `@app.get("/path")` | GET | Read / fetch data |
| `@app.post("/path")` | POST | Send data / create |
| `@app.put("/path")` | PUT | Update existing data |
| `@app.delete("/path")` | DELETE | Remove data |

---

## Step 8.1 — Hello World

```python
from fastapi import FastAPI

# create the server instance
app = FastAPI()

# GET route at "/"
# when someone visits http://localhost:8000/ this function runs
@app.get("/")
def root():
    return {"message": "Hello World"}  # sent back as JSON automatically
```

Test URLs:
- `http://localhost:8000/` → JSON response
- `http://localhost:8000/docs` → auto-generated interactive docs

---

## Step 8.2 — POST route with request body

```python
from pydantic import BaseModel

# defines what the request body must look like
class ChatRequest(BaseModel):
    message: str  # expects {"message": "some text"}

# POST route at "/chat"
# req is automatically parsed from the request body JSON
@app.post("/chat")
def chat(req: ChatRequest):
    return {"you_said": req.message, "length": len(req.message)}
```

Test in Thunder Client:
- Method: `POST`
- URL: `http://localhost:8000/chat`
- Body (JSON): `{"message": "Hello Gemini"}`

---

## Step 8.3 — Path parameter

```python
# {name} in the URL becomes a variable in the function
@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello {name}!"}
```

Test: visit `http://localhost:8000/greet/Pravat` in browser.

---

## Step 8.4 — Full REST pattern (GET + POST + DELETE)

```python
messages = []

@app.post("/messages")
def add_message(req: ChatRequest):
    messages.append(req.message)
    return {"stored": req.message, "total": len(messages)}

@app.get("/messages")
def get_messages():
    return {"messages": messages}

@app.delete("/messages")
def delete_messages():
    messages.clear()
    return {"status": "all messages deleted"}
```

---

## How a request flows through FastAPI

```
Client sends:
POST /chat
{"message": "What is Python?"}
        ↓
FastAPI receives it
        ↓
Pydantic validates → converts to ChatRequest object
        ↓
Your chat() function runs
        ↓
Returns a dict or Pydantic model
        ↓
FastAPI converts to JSON and sends back:
{"reply": "Python is..."}
```

---

## Build order

| Step | What you build | What you learn |
|------|---------------|----------------|
| 8.1 | Hello World GET | Routes + decorators |
| 8.2 | POST with body | Pydantic + request body |
| 8.3 | Path parameter | Dynamic URLs |
| 8.4 | GET + POST + DELETE | Full REST pattern |
| 8.5 | Wire in Gemini | Complete chatbot API |

---

## FastAPI Cheatsheet

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET — read data
@app.get("/items")
def get_items():
    return {"items": []}

# POST — receive JSON body
class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return {"created": item.name}

# Path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}
```

---

## Key URLs when server is running

| URL | What it shows |
|-----|--------------|
| `http://localhost:8000/` | Your root endpoint |
| `http://localhost:8000/docs` | Swagger interactive docs |
| `http://localhost:8000/redoc` | Alternative docs view |
