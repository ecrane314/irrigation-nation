#!/usr/bin/env python3

"""Get sunset and sunrise time for a lattitude and longitude
For example, 30.267238, -97.755202
Data are provided via API from https://sunrise-sunset.org/api
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

Evan Crane May 2020
"""

import requests
# https://requests.readthedocs.io/en/v0.6.2/api/
import json

def get_sunrise_sunset(lat=30.267238, lng=-97.755202, civil=0, nautical=0):
    """Input lattitude and longitude and return sunrise and sunset times"""
    request_body = "https://api.sunrise-sunset.org/json?lat=%f&lng=%f" % (lat, lng)
    print("Request body: " + request_body)

    response = requests.get(request_body)
    print(type(response))

    print(response.content)

    return response

if __name__ == "__main__":
    get_sunrise_sunset()
