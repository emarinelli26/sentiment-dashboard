# main.py
from reddit_client import create_reddit_client
from fetch_posts import fetch_posts, fetch_comments_from_post
from sentiment_analysis import analyze_sentiment
import pandas as pd
import os

def main():
    reddit = create_reddit_client()
    keyword = input("🔍 Ingresá una palabra clave para buscar: ")
    posts = fetch_posts(reddit, keyword, limit=3)

    results = []

    for post in posts:
        comments = fetch_comments_from_post(post)
        for comment in comments:
            sentiment, polarity = analyze_sentiment(comment)
            results.append({
                "post_title": post.title,
                "comment": comment,
                "sentiment": sentiment,
                "polarity": polarity,
                "url": post.url
            })

    # Guardar resultados
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv(f"data/resultados_{keyword}.csv", index=False, encoding='utf-8')
    print(f"\n✅ Análisis completo. Resultados guardados en data/resultados_{keyword}.csv")

if __name__ == "__main__":
    main()