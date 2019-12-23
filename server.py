import json
import logging
import os
import sqlite3

from flask import g
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func


DATABASE = 'cryptid.db'
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(DATABASE)
db = SQLAlchemy(app)


# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db


# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()


@app.route('/')
def index():
    return render_template('index.html')


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String, unique=False, nullable=False)
    user = db.Column(db.String, unique=False, nullable=False)
    url = db.Column(db.String, unique=False, nullable=False)


@app.route('/api/log/', methods=["POST"])
def log_visit():
    data = request.json
    app.logger.info(data)

    db.session.add(Log(timestamp=data['timestamp'], user=data['user'], url=data['url']))
    db.session.commit()
    # with app.app_context():
    #     cur = get_db().cursor()

    return jsonify([])


@app.route('/api/log/', methods=["GET"])
def get_log():
    visits = Log.query.with_entities(Log.user, func.count(Log.user)).group_by(Log.user).all()
    print("visits", visits)

    return jsonify([serialize_log(entry) for entry in visits])


def serialize_log(entry):
    print("entry", entry)
    return {
        "user": entry[0],
        "visits": entry[1],
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
