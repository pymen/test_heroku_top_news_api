"""Module for helper functions"""

from os import environ

import requests


def get_top_news():
    """Makes sync request to api to get,
     on success: returns json
     on failure: raises exception
     """
    api_key = environ.get("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?sources=reddit-r-all&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
