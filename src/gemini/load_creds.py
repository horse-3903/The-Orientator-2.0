import os
from dotenv import load_dotenv

import google.generativeai as genai
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

def load_creds():
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

    return creds