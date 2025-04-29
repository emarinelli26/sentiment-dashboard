def search_videos(youtube, query, max_results=3):
    request = youtube.search().list(
        part="id,snippet",
        q=query,
        type="video",
        maxResults=max_results
    )
    response = request.execute()
    videos = []
    for item in response.get('items', []):
        videos.append({
            "video_id": item['id']['videoId'],
            "title": item['snippet']['title']
        })
    return videos

def fetch_comments(youtube, video_id, max_comments=20):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=min(max_comments, 100),  # Máximo 100 por request
        textFormat="plainText"
    )
    response = request.execute()

    comments = []
    for item in response.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    return comments
