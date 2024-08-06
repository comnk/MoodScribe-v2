from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import config
import pyttsx3

import json

app = Flask(__name__)
CORS(app)

engine = pyttsx3.init()

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
    #engine.say(quote['content'])
    #engine.say("By " + quote['author'])
    #engine.runAndWait() 
    return jsonify({"message": quote['content'], "author": quote['author']})

@app.route('/api/speak', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('message')
    # Call your text-to-speech function and return the result
    if (text):
        engine.say(text)
        engine.runAndWait()
        return jsonify({"status": "success", "message": "Text spoken successfully"})
    else:
        return jsonify({"status": "error", "message": "No text provided"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=8080)