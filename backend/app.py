from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    response = jsonify(message="ping")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response