from flask import Flask, jsonify, json
from werkzeug import exceptions

from utils import get_top_news

app = Flask(__name__)


@app.errorhandler(exceptions.HTTPException)
def http_exception(error):
    """Flask Error handler for all types of HTTP exceptions"""
    data = {'error': str(error)}
    return app.response_class(
            response=json.dumps(data),
            status=error.code,
            mimetype='application/json'
        )


@app.route('/')
def top_news():
    """Return top news from news api"""
    data = get_top_news()
    return jsonify(data)


if __name__ == '__main__':
    app.run()
