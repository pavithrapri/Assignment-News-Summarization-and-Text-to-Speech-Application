import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS
import nltk
from collections import Counter

nltk.download('punkt')

API_KEY = "a01a797186aa44edb05dcb985a92b2a7"

def fetch_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&apiKey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return [], {}, "No articles found."
    
    data = response.json()
    articles = data.get("articles", [])[:10]
    
    processed_articles = []
    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in articles:
        title = article.get("title", "No Title")
        content = extract_article_content(article.get("url", ""))
        
        sentiment = analyze_sentiment(content)
        topics = extract_topics(content)

        processed_articles.append({
            "Title": title,
            "Summary": content[:200],
            "Sentiment": sentiment,
            "Topics": topics
        })

        sentiment_count[sentiment] += 1

    final_sentiment = max(sentiment_count, key=sentiment_count.get)

    return processed_articles, sentiment_count, final_sentiment

def extract_article_content(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join([p.text for p in paragraphs]) if paragraphs else "Content not available."
    except:
        return "Error fetching content."

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    return "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

def extract_topics(text):
    words = nltk.word_tokenize(text.lower())
    common_words = [word for word in words if word.isalpha()]
    return [word for word, count in Counter(common_words).most_common(5)]

def generate_tts(text, filename):
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename
