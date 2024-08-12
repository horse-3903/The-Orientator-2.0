import os
import json
import time

from tqdm import tqdm
# from dotenv import load_dotenv

import google.generativeai as genai
# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow

from load_creds import load_creds

load_creds()

name = "test-model-5"

model = genai.GenerativeModel(model_name=f"tunedModels/{name}")

with open("./data/final_data.json", "r") as f:
    data = json.loads(f.read())

if not os.path.exists(f"./test/{name}.txt"):
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
