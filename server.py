import json
import os

from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/log/')
def log_visit():
    print("test")
    return jsonify([])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
