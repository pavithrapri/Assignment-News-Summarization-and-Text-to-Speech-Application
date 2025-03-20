from flask import Flask, request, jsonify
from utils import fetch_news, analyze_sentiment, generate_tts

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    company = data.get("company")

    if not company:
        return jsonify({"error": "Company name is required."}), 400

    articles, sentiment_count, final_sentiment = fetch_news(company)
    summary_text = f"{company} has {sentiment_count['Positive']} positive, {sentiment_count['Negative']} negative, and {sentiment_count['Neutral']} neutral news articles."
    
    tts_file = generate_tts(summary_text, "output.mp3")

    result = {
        "Company": company,
        "Articles": articles,
        "Sentiment Score": sentiment_count,
        "Final Sentiment": final_sentiment,
        "Audio": tts_file
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
