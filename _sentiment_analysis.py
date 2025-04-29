from textblob import TextBlob

def analyze_sentiment(text):
    try:
        # Intentamos traducir al inglés
        blob = TextBlob(text)
        translated = blob.translate(to='en')
        polarity = translated.sentiment.polarity
    except Exception:
        # Si falla la traducción, usamos el texto original
        polarity = TextBlob(text).sentiment.polarity

    # Clasificamos el sentimiento
    if polarity > 0:
        sentiment = "positivo"
    elif polarity < 0:
        sentiment = "negativo"
    else:
        sentiment = "neutro"
    return sentiment, polarity
