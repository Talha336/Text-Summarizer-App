from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Main route for rendering the UI
@app.route('/')
def index():
    return render_template('index.html')

# Summarization endpoint
@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form.get("text")
    if not input_text:
        return jsonify({"error": "No input text provided"}), 400

    api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {
        "Authorization": "Bearer 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",  # Correct API key format
        "Content-Type": "application/json"
    }

    payload = {"inputs": input_text}

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        summary = response.json()[0].get("summary_text", "No summary returned.")
        return jsonify({"summary": summary})
    else:
        error_message = response.json().get("error", "Failed to summarize text")
        return jsonify({"error": error_message}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
