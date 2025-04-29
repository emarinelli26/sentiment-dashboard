from googleapiclient.discovery import build

def create_youtube_client(api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    return youtube