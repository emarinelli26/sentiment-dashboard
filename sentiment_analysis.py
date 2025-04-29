from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    try:
        # Traducimos al inglés
        translated = TextBlob(text).translate(to='en')
        text_en = str(translated)
    except Exception:
        text_en = text  # Si no se puede traducir, usamos el original

    # Análisis con VADER
    scores = analyzer.polarity_scores(text_en)
    compound = scores['compound']

    # Clasificación
    if compound >= 0.05:
        sentiment = "positivo"
    elif compound <= -0.05:
        sentiment = "negativo"
    else:
        sentiment = "neutro"

    return sentiment, compound
