import json

import requests
from flask import Flask, jsonify
from os import environ

app = Flask(__name__)


@app.route('/')
def top_news():
    """Return top news from newsapi"""
    api_key = environ.get('NEWS_API_KEY')
    url = f"https://newsapi.org/v2/top-headlines?sources=reddit-r-all&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        data = {'error': response.content}
        return app.response_class(
            response=json.dumps(data),
            status=response.status_code,
            mimetype='application/json'
        )


if __name__ == '__main__':
    app.run()
