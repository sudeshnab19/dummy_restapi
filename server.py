from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def server_root():
    data = {"message": "This is server roots"}
    return jsonify(data), 200


@app.route("/name/<name>")
def name_process(name: str):
    data = {"message": name}
    return jsonify(data), 200
