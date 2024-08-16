import os

import time
import json

from load_creds import load_creds

import random

import google.generativeai as genai
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

creds = load_creds()

genai.configure(credentials=creds)

base_model = [m for m in genai.list_models() if "createTunedModel" in m.supported_generation_methods][0]
base_model

with open(os.getenv("PARENT_DIR") + "data/final_data.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

    training_data = [{"text_input": a, "output": b} for a, b in data]

name = "test-model-13"
operation = genai.create_tuned_model(
    source_model=base_model.name,
    training_data=training_data,
    id = name,
    epoch_count = 100,
    batch_size = 4,
    learning_rate = 0.0001,
)

name = "test-model-4"
model = genai.get_tuned_model(f"tunedModels/{name}")

model = genai.GenerativeModel(model_name=f"tunedModels/{name}")

# for status in operation.wait_bar():
#     time.sleep(2)

content = model.generate_content("What can I do leisurely in HCI?")
print(content.text)