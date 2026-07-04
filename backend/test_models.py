import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your secure key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("Asking Google for your approved models...\n")

# Loop through and print every model this key is allowed to use
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)