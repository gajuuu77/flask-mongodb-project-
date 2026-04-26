from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient

app = Flask(__name__)

# 🔹 MongoDB Atlas Connection (replace with your URL)
client = MongoClient("your_mongodb_connection_string")
db = client["testdb"]
collection = db["students"]

# 🔹 API Route
@app.route('/api')
def get_data():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)
