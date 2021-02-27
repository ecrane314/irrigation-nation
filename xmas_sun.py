#!/usr/bin/env python3

"""Get sunset and sunrise time for a lattitude and longitude
For example, 30.267238, -97.755202
Data are provided via API from https://sunrise-sunset.org/api
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

Evan Crane May 2020
"""

import json
import sys
import requests
# https://requests.readthedocs.io/en/v0.6.2/api/


def get_solar_data(lat=30.267238, lng=-97.755202):
    """Input lattitude and longitude and return sunrise and sunset times"""
    #request includes lat and long, formatting turned off here, on by default
    request_body = "https://api.sunrise-sunset.org/json?lat=%f&lng=%f&formatted=0" % (lat, lng)
    #   print("Request body: " + request_body)

    response = requests.get(request_body)
    print(response)
    print("================")
    print(response.content)
    print("================")

    return response.content


def extract_phase(phase_data, phase="sunrise"):
    """Extract a particular phase from the JSON API response"""
    #load json response to dict with phases
    parse = json.loads(phase_data)

    print("In extract fn: " + phase)
    #print(list(parse))

    try:
        #TODO Add time zone shift for system time.
        return parse["results"][phase]
    except KeyError:
        print("No phase named: " + phase)


if __name__ == "__main__":
    try:
        in_phase = sys.argv[1]
        print("Main try argv: " + in_phase)
        print(extract_phase(get_solar_data(), phase=in_phase))
    except AttributeError:
        print("=== Exception loop! ===")
        print(extract_phase(get_solar_data()))
