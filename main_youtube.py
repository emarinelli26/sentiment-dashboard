from youtube_client import create_youtube_client
from fetch_youtube import search_videos, fetch_comments
from sentiment_analysis import analyze_sentiment
import pandas as pd
import os

def main():
    # Reemplazá esta línea por tu API KEY real
    API_KEY = "TU_API_KEY"
    youtube = create_youtube_client(API_KEY)

    # Palabra clave que queremos buscar
    query = "Guillermo Moreno"

    # Sanitizar el nombre del archivo (sin espacios)
    filename_query = query.replace(" ", "_").lower()

    videos = search_videos(youtube, query, max_results=3)

    results = []

    for video in videos:
        comments = fetch_comments(youtube, video['video_id'], max_comments=20)
        for comment in comments:
            sentiment, polarity = analyze_sentiment(comment)
            results.append({
                "video_title": video['title'],
                "comment": comment,
                "sentiment": sentiment,
                "polarity": polarity,
                "video_url": f"https://www.youtube.com/watch?v={video['video_id']}"
            })

    # Crear carpeta data si no existe
    os.makedirs("data", exist_ok=True)

    # Guardar resultados en CSV con nombre dinámico
    output_path = f"data/resultados_youtube_{filename_query}.csv"
    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"\n✅ Análisis completo. Resultados guardados en {output_path}")

if __name__ == "__main__":
    main()
