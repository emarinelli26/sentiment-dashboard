# fetch_posts.py
def fetch_posts(reddit, keyword, limit=5):
    posts = []
    for post in reddit.subreddit("all").search(keyword, limit=limit):
        posts.append(post)
    return posts

def fetch_comments_from_post(post, limit=10):
    post.comments.replace_more(limit=0)  # Evita "load more"
    return [comment.body for comment in post.comments.list()[:limit]]
