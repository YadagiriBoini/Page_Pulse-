from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import time
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    if not url.startswith("http"):
        url = "https://" + url

    try:

        start = time.time()

        response = requests.get(url, timeout=10)

        end = time.time()

        response_time = round((end - start) * 1000)

        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type:
            return jsonify({"error": "Non HTML page"}), 400

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No title"

        meta = soup.find("meta", attrs={"name": "description"})
        description = (
            meta["content"] if meta and meta.get("content") else "No description"
        )

        h1_count = len(soup.find_all("h1"))

        images = soup.find_all("img")
        missing_alt = sum(1 for img in images if not img.get("alt"))

        words = soup.get_text(separator=" ").split()

        return jsonify(
            {
                "status": response.status_code,
                "response_time": f"{response_time} ms",
                "title": title,
                "description": description,
                "h1_count": h1_count,
                "missing_alt": missing_alt,
                "word_count": len(words),
            }
        )

    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timed out"}), 408

    except requests.exceptions.RequestException:
        return jsonify({"error": "Invalid URL"}), 400


if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
