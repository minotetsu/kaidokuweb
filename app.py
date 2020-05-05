import numpy as np
import main
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def param_nothing():
    ret = main.main(1)
    html = render_template('home.html', ret=ret)
    return html

@app.route('/<json_number>')
def parm_exist(json_number=None):
    ret = main.main(json_number)
    html = render_template('home.html', ret=ret)
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
