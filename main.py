import requests
import pandas as pd
from time import sleep
from dotenv import load_dotenv
import os

# ========== CONFIG ==========
# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")

BASE_URL = "https://www.googleapis.com/youtube/v3"

# ========== STEP 1: Get Uploads Playlist ID from Channel ==========
def get_uploads_playlist_id(api_key, channel_id):
    url = f"{BASE_URL}/channels"
    params = {
        "part": "contentDetails",
        "id": channel_id,
        "key": api_key
    }

    res = requests.get(url, params=params)
    data = res.json()
    try:
        uploads_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return uploads_id
    except (IndexError, KeyError):
        print("Error fetching uploads playlist ID:", data)
        return None

# ========== STEP 2: Get All Video IDs from Uploads Playlist ==========
def get_video_ids(api_key, uploads_id):
    video_ids = []
    url = f"{BASE_URL}/playlistItems"
    params = {
        "part": "contentDetails",
        "playlistId": uploads_id,
        "maxResults": 50,
        "key": api_key
    }

    while True:
        res = requests.get(url, params=params)
        data = res.json()

        for item in data.get('items', []):
            video_ids.append(item['contentDetails']['videoId'])

        if 'nextPageToken' in data:
            params['pageToken'] = data['nextPageToken']
            sleep(0.1)
        else:
            break

    return video_ids

# ========== STEP 3: Get Video Stats ==========
def get_video_details(api_key, video_ids):
    video_data = []
    url = f"{BASE_URL}/videos"

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        params = {
            "part": "snippet,statistics,contentDetails",
            "id": ",".join(batch),
            "key": api_key
        }

        res = requests.get(url, params=params)
        data = res.json()

        for item in data.get('items', []):
            video_info = {
                "video_id": item['id'],
                "title": item['snippet']['title'],
                "published_at": item['snippet']['publishedAt'],
                "views": item['statistics'].get('viewCount', 0),
                "likes": item['statistics'].get('likeCount', 0),
                "comments": item['statistics'].get('commentCount', 0),
                "duration": item['contentDetails']['duration']
            }
            video_data.append(video_info)

    return video_data

# ========== STEP 4: Run & Save ==========
if __name__ == "__main__":
    print("Fetching uploads playlist ID...")
    uploads_playlist_id = get_uploads_playlist_id(API_KEY, CHANNEL_ID)

    if uploads_playlist_id:
        print("Fetching video IDs...")
        video_ids = get_video_ids(API_KEY, uploads_playlist_id)
        print(f"Total videos: {len(video_ids)}")

        print("Fetching video details...")
        video_data = get_video_details(API_KEY, video_ids)

        df = pd.DataFrame(video_data)
        print(df.head())

        df.to_csv("youtube_channel_data.csv", index=False)
        print("Data exported to 'youtube_channel_data.csv'")
