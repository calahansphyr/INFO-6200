"""
Minimal Flask web app. To run:
  1. pip install flask
  2. python web_app.py
Then open http://127.0.0.1:5000/
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """View function for the root URL."""
    return "Hello, Web!"


if __name__ == "__main__":
    app.run(debug=True)
