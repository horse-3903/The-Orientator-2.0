import os
import json

from load_creds import load_creds
import google.generativeai as genai

creds = load_creds()
genai.configure(credentials=load_creds())

name = "gemini-1.5-pro"
model = genai.GenerativeModel(name, generation_config={"response_mime_type": "application/json"})

prompt = """List me at least 5 different questions to a single answer
The original question {question}, and the answer is {answer}

In the JSON schema of :
response = {"question" : {answer}}

Return a `list[response]`
"""

with open(os.getenv("PARENT_DIR") + "data/final_data.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

    training_data = [{"text_input": a, "output": b} for a, b in data]