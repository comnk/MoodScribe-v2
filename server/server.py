from flask import Flask, jsonify
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import config

import json

app = Flask(__name__)
CORS(app)

uri = config.MONGODB_KEY
client = MongoClient(uri, server_api=ServerApi('1'))

@app.route("/api/test", methods=["GET"])
def test():
    collection_name = client["sample_mflix"]["comments"]
    item_details = collection_name.find()
    items = []

    for item in item_details:
        items.append(item)

    return jsonify({"message": "Hello World", "items":json.loads(json.dumps(items, default=str))})

@app.route("/api/generate_quote", methods=["GET"])
def get_quote():
    response = requests.get('https://api.quotable.io/random')
    quote = response.json()
    print(quote['content'], quote['author'])
    return jsonify({"message": quote['content'], "author": quote['author']})

if __name__ == "__main__":
    app.run(debug=True, port=8080)