#!/usr/bin/env python3

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/time")
def current_time():
    return "The current time is " + str(datetime.now())

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
