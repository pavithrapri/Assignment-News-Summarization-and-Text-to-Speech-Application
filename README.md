# Assignment-News-Summarization-and-Text-to-Speech-Application


News Summarization & Sentiment Analysis with Hindi TTS

Project Overview

This web-based application extracts news articles for a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. Users can enter a company name, and the application will return a structured sentiment report along with a playable Hindi audio summary.

1️⃣ Project Setup

Prerequisites

Ensure you have Python installed (>= 3.7). Also, install dependencies using:

Running the Application

Start the Flask API

The API will be available at http://127.0.0.1:5000/analyze.

Start the Streamlit UI

2️⃣ Model Details

News Summarization:

We use BeautifulSoup to scrape and extract relevant article content.

The summaries are created by extracting key paragraphs and truncating them to 200 characters.

Sentiment Analysis:

We use TextBlob, a lightweight NLP tool, to determine the sentiment of each article.

The polarity score classifies articles as:

Positive (score > 0)

Negative (score < 0)

Neutral (score = 0)

Text-to-Speech (TTS):

We use gTTS (Google Text-to-Speech) to convert the sentiment summary into Hindi audio.

The generated speech file is saved as output.mp3 and played in the UI.

3️⃣ API Development

API Request Format

Endpoint: http://127.0.0.1:5000/analyze

Request Body (JSON):

API Response Format

Testing via Postman

Open Postman.

Create a POST request to http://127.0.0.1:5000/analyze.

Go to the Body tab → raw → JSON and enter:

Click Send. You will receive a structured JSON response with sentiment analysis and a link to the generated audio file.

4️⃣ API Usage (Third-Party APIs Used)

1. NewsAPI

Purpose: Fetches 10 latest news articles for a given company.

Integration:

Sign up at NewsAPI to get an API key.

Replace API_KEY = "your_newsapi_key_here" in utils.py.

2. gTTS (Google Text-to-Speech)

Purpose: Converts the final sentiment summary into Hindi audio.

Integration: Installed as a Python library (pip install gtts).

The generate_tts() function in utils.py creates an audio file (output.mp3).

5️⃣ Assumptions & Limitations

Assumptions:

NewsAPI provides relevant and recent news for the given company.

Sentiment analysis is based on article content and might not always reflect real-world sentiment.

Hindi TTS accurately conveys the sentiment summary.

Limitations:

NewsAPI Free Tier Restriction – Limited to 100 requests per day.

BeautifulSoup Limitation – Only works with non-JavaScript-rendered pages.

TextBlob Sentiment Accuracy – May not fully capture sarcasm or complex sentiment nuances.

Audio Output – gTTS requires an internet connection to generate Hindi speech.


