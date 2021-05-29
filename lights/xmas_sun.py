#!/usr/bin/env python3

"""Get sunset and sunrise time for a lattitude and longitude
For example, 30.267238, -97.755202
Data are provided via API from https://sunrise-sunset.org/api
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
Evan Crane - Starting May 2020
"""

import json
import sys
import logging
from activate_lights import activate_lights as lights
#TODO import argparse #for lat lng
from datetime import datetime, timezone

import requests
# https://requests.readthedocs.io/en/v0.6.2/api/


logger = logging.getLogger(__name__)
logging.basicConfig(filename="xmas_sun.log")


def get_solar_data(lat=30.267238, lng=-97.755202):
    """Input lattitude and longitude and return sunrise and sunset times"""
    
    # Define request, includes lat and long, formatting off here
    request_body = "https://api.sunrise-sunset.org/json?\
lat=%f&lng=%f&formatted=0" % (lat, lng)
    print("Request body: " + request_body)

    # Get and return response
    response = requests.get(request_body)
    print("=======response=========")
    print(response)
    print("=======response.content=========")
    print(response.content)
    return response.content


def extract_phase(phase_data, phase="sunset"):
    """Extract a particular phase from the JSON API response"""
    #loads json response to dict with phases
    parse = json.loads(phase_data)
    print("extract_phase, phase: " + phase)

    #return phase
    try:
        #TODO Add time zone shift for system time.
        return parse["results"][phase]
    except KeyError:
        print("No phase named: " + phase)
        return None


def golden_hour()
    #sunset_tod_in_seconds =    #time of day
    #gh_begins = sunset_tod_in_seconds - 3600
    # run lights for 3600 seconds at gh_begins??

def phase_to_seconds()
    #TODO not sure if needed


def utc_to_local(utc_dt):
    """BROKEN, Convert UTC time to local time"""
    # Sample datetime 2021-03-01T00:29:45+00:00
    #TODO Fixme
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(timezo=None)


def as_timezone(self, timezo):
    """SCRATCH, unclear what's happening here"""
    if self.tzinfo is timezo:
        return self
    
    # Convert self to UTC, and attach the new time zone object.
    utc = (self - self.utcoffset()).replace(tzinfo=timezo)
    
    # Convert from UTC to timezo's local time.
    return timezo.fromutc- Starting (utc)


if __name__ == "__main__":
    try:
        user_phase = sys.argv[1]
        #lights(5)
        print("Main loop argv[1]: " + user_phase)
        print(extract_phase(get_solar_data(), phase=user_phase))
    except IndexError:
        print("=== Exception loop! ===")
        print(extract_phase(get_solar_data()))
