import os
import json
import time

from tqdm import tqdm
from dotenv import load_dotenv

import google.generativeai as genai
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/cloud-platform", "https://www.googleapis.com/auth/generative-language.tuning"]
KEY_FILE = os.getenv("PARENT_DIR") + "auth/credentials.json"
TOKEN_FILE = os.getenv("PARENT_DIR") + "auth/token.json"

# auth stuff, ugh
creds = None

if os.path.exists(TOKEN_FILE):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(KEY_FILE, SCOPES)
        creds = flow.run_local_server()
    
    with open(TOKEN_FILE, "w") as token:
        token.write(creds.to_json())

genai.configure(credentials=creds)        

# code starts here

# for model_info in genai.list_tuned_models():
#     print(model_info)

name = "test-model-5"

model = genai.GenerativeModel(model_name=f"tunedModels/{name}")

with open("./data/final_data.json", "r") as f:
    data = json.loads(f.read())

with open(f"./test/{name}.txt", "w+") as f:
    f.write("")

for question, answer in tqdm(data[54:]):
    try:
        content = model.generate_content(question)
    except:
        print("\nQuota reached! Waiting...")
        time.sleep(4)

    res = f"Question : {question}\n"
    res += f"Training answer : {answer}\n"
    res += f"Validation answer : {content.text}\n\n"

    with open(f"./test/{name}.txt", "a", encoding="utf-8") as f:
        f.write(res)
