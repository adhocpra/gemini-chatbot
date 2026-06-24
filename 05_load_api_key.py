import os
from dotenv import load_dotenv
#load_dotenv function reas env file

load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")

if api_key:
    print("key loaded successfully")
    print(f"Key starts with: {api_key[:8]}...")
    #slices the first 8 characters of the key string. Just the start is printed to verify 
else:
    print("Key not found--check your .env file")