import db
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/init_db', methods=['POST'])
def init_database():
    db.init_db()
    return "OK\n"


@app.route('/create_user', methods=['POST'])
def create_user():
    if not request.is_json:
        return "Wrong JSON\n"
    content = request.get_json()
    print(content)
    db.save_user(content)
    return "OK\n"


@app.route('/get_users', methods=['GET'])
def get_users():
    return json.dumps({"users" : db.get_users()})
