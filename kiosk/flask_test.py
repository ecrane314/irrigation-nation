#!/usr/bin/env python3

"""
Flask UI app
"""

from datetime import datetime
import requests
import sys

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Base Hello World"""
    return "Hello, World!"

@app.route("/time")
    """Route to display current time"""
def current_time():
    return "The current time is " + str(datetime.now())

@app.route("/spx")
    """Route to get current price for SP500"""
def get_spx():
#TODO Get key from environment variable. Pull from finnhub.io 
    #    key = sys.
    return 

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
