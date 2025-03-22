import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from googleapiclient.discovery import build
from .youtube_auth import get_authenticated_service
import os
import time
from dotenv import load_dotenv

load_dotenv()

def get_spotify_tracks(playlist_url):
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
    ))

    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = []

    for item in results['items']:
        track = item['track']
        if track:
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            tracks.append(f"{track_name} {artist_name}")

    return tracks

def search_youtube_music(youtube, query):
    search_response = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=1,
        type="video"
    ).execute()

    items = search_response.get("items")
    if items:
        return items[0]["id"]["videoId"]
    return None

def create_youtube_playlist(youtube, title):
    playlist = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "Playlist generated from Spotify playlist"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    ).execute()
    return playlist["id"]

def add_video_to_playlist(youtube, playlist_id, video_id):
    youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    ).execute()

def convert_spotify_to_youtube(spotify_url):
    youtube = get_authenticated_service()
    tracks = get_spotify_tracks(spotify_url)

    video_ids = []
    for track in tracks:
        video_id = search_youtube_music(youtube, track)
        if video_id:
            video_ids.append(video_id)
        time.sleep(0.3)

    playlist_id = create_youtube_playlist(youtube, "Converted from Spotify 🎵")
    for vid in video_ids:
        add_video_to_playlist(youtube, playlist_id, vid)

    return {
        "playlist_url": f"https://music.youtube.com/playlist?list={playlist_id}"
    }
