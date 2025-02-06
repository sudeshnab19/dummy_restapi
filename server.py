from flask import Flask, jsonify
from json import load

app = Flask(__name__)

@app.route("/")
def server_root():
    data = {"message": "This is server roots"}
    return jsonify(data), 200


@app.route("/name/<name>")
def name_process(name: str):
    data = {"message": name}
    return jsonify(data), 200


@app.route("/weather/nyc")
def weather_nyc():
    data = None
    with open("./data/data.json") as f:
        data = load(f)
    return jsonify(data), 200
