import numpy as np
import main
from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/kaidoku", methods=["POST"])
def kaidoku():
    request_data = request.get_json()
    question = request_data["numbers"]
    ret = main.main(question)
    ret_json = jsonify({"result": ret[0], "numbers": ret[1]})
    return ret_json

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
