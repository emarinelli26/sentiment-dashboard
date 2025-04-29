# reddit_client.py
import praw

def create_reddit_client():
    reddit = praw.Reddit(
        client_id="Ro1LGVwbtQUv-WfQXu38GA",
        client_secret="stUpmRBRassgrF3qFrMfPpCgDt2eSw",
        user_agent="test-script-by-emanuel"
    )
    return reddit