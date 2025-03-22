
# 🎵 Spotify to YouTube Music Converter

Convert a **Spotify playlist** into a **YouTube Music playlist** — using a modern Angular + Django web app.

Paste a Spotify playlist URL, and get back a YouTube Music playlist link with the same songs!

---

## 🚀 Features

- 🔄 Converts Spotify playlist → YouTube Music
- 🔐 Uses YouTube OAuth for playlist creation (avoids API quota issues)
- 🧠 Backend: Python + Django + REST
- 💻 Frontend: Angular with live link + copy button
- 🌙 Dark UI

---

## 🧰 Tech Stack

| Layer        | Tech                         |
|--------------|------------------------------|
| Frontend     | Angular                      |
| Backend      | Django + Django REST         |
| APIs Used    | Spotify Web API, YouTube Data API v3 |
| OAuth        | Google Auth (OAuth 2.0)      |
| Python Libs  | spotipy, google-auth-oauthlib, google-api-python-client |

---

## ⚙️ Prerequisites

### 1️⃣ Spotify API Setup

1. Go to: [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app.
3. Get the **Client ID** and **Client Secret**.
4. Add the following Redirect URI under app settings:
   ```
   http://localhost:8000/callback/
   ```

### 2️⃣ Google Cloud OAuth Setup (YouTube API)

1. Visit: [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or use an existing one.
3. Go to **APIs & Services → Library**, and enable:
   - ✅ YouTube Data API v3

4. Then go to **Credentials** → `+ Create Credentials` → **OAuth client ID**:
   - Choose: **Desktop App**
   - Download the generated JSON (e.g., `client_secret_*.json`)
   - Rename to: `client_secret.json`

5. Move this file to:
   ```
   backend/converter/client_secret.json
   ```

6. Also go to **OAuth Consent Screen**, fill basic app info, and add your email as a **test user**.

---

## 🛠️ Local Setup Instructions

### 📁 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/spotify-to-ytmusic.git
cd spotify-to-ytmusic
```

---

### 🖥️ 2. Backend Setup (Django)

```bash
cd backend

```bash
pip install django djangorestframework django-cors-headers spotipy google-auth google-auth-oauthlib google-api-python-client python-dotenv
```

#### 🔐 Set up environment variables

Create a `.env` file in the **project root** (same level as `backend/`) and add:

```env
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

Or copy the included `.env.example` and fill in your credentials:

```bash
cp backend/backend/.env.example .env
```

---

#### 🔑 Run OAuth Flow (only once)

```bash
python backend/converter/youtube_auth.py
```

- This will open a browser asking for permission.
- After accepting, it saves `youtube_oauth.json` locally (used by the app).

---

#### ▶️ Start Django Backend

```bash
python manage.py runserver
```

Django will run at:  
**http://127.0.0.1:8000/**

---

### 🌐 3. Frontend Setup (Angular)

```bash
cd spotify-to-ytmusic-frontend
npm install
ng serve
```

Angular will run at:  
**http://localhost:4200/**

---

## 🧪 How to Use

1. Open the frontend in your browser: `http://localhost:4200`
2. Paste any public Spotify playlist URL.
3. Click **Convert**.
4. After a few seconds, your YouTube Music playlist link appears!
5. Click 📋 to copy it and share.

---

## ❓ Common Questions

### 🔹 Why do I need OAuth for YouTube?

YouTube's API requires **OAuth login** to allow playlist creation on your behalf. API keys alone **cannot create playlists**.

### 🔹 Do I need to publish my Google App?

No — for local use, just add your email as a **test user** in OAuth Consent Screen.

### 🔹 Can I share this app with friends?

Yes, but they must:
- Set up their own **Spotify** and **Google** credentials
- Run OAuth flow on their machine

Unless you **go through OAuth verification** with Google, the app is for **development/testing use only**.

---

## 📦 Folder Structure

```
spotify-to-ytmusic/
│
├── backend/                      # Django backend
│   └── converter/               # Django app logic
│       ├── youtube_auth.py      # Handles YouTube OAuth login
│       ├── utils.py             # Spotify + YouTube logic
│       ├── views.py             # API view
│       └── ...
│
├── spotify-to-ytmusic-frontend/ # Angular frontend
│   └── src/
│       └── app/
│           └── playlist-converter/   # UI Component
│               ├── .html
│               ├── .ts
│               └── .css
```

---

## 📝 License

This project is for **educational purposes only** and is not affiliated with Spotify or Google.

---

## 🙏 Credits

Made with ❤️ by Rohith  
Powered by Open Source APIs + Frameworks
