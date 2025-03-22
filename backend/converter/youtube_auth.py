import os
import json
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service():
    CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

    if os.path.exists("youtube_oauth.json"):
        with open("youtube_oauth.json", "r") as f:
            credentials_data = json.load(f)
        from google.oauth2.credentials import Credentials
        credentials = Credentials.from_authorized_user_info(credentials_data, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_config(
            {
                "installed": {
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token"
                }
            },
            SCOPES
        )
        credentials = flow.run_local_server(port=8080)
        with open("youtube_oauth.json", "w") as f:
            f.write(credentials.to_json())

    return build("youtube", "v3", credentials=credentials)

# Optional testing
if __name__ == "__main__":
    print("Authenticating YouTube...")
    get_authenticated_service()
