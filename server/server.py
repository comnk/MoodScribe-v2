from flask import Flask, jsonify
from flask_cors import CORS

import pymongo

app = Flask(__name__)
CORS(app)

@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello World", "people":["Jack", "Barry", "Harry"]})

if __name__ == "__main__":
    app.run(debug=True, port=8080)