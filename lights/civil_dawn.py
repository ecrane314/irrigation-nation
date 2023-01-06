#!/usr/bin/env python3

"""Get sunset and sunrise time for a lattitude and longitude
returns civil dawn, which is when sun is 6 degrees below horizon
location in lat_lng.config
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

Data provided via https://sunrise-sunset.org/api
Evan Crane - Starting May 2020
"""

import json
import sys
import logging

#TODO import argparse #for lat lng
from datetime import datetime, timezone

import requests


logger = logging.getLogger(__name__)
logging.basicConfig(filename="civil_dawn.log", level="DEBUG", format="%(asctime)s %(levelname)s %(message)s")


def get_solar_data(lat=30.267238, lng=-97.755202):
    """Input lattitude and longitude and return sunrise and sunset times"""
    
    # Define request, includes lat and long, formatting off here
    request_body = "https://api.sunrise-sunset.org/json?\
lat=%f&lng=%f&formatted=0" % (lat, lng)
    logger.info("Request body: " + request_body)

    # Get and return response
    response = requests.get(request_body)
    logger.debug(response.content)

    return response.content


def extract_phase(phase_data, phase="sunset"):
    """Extract a particular phase from the JSON API response"""
    #loads json response to dict with phases
    parsed = json.loads(phase_data)

    #return phase
    try:
        #TODO return with time zone shift for system time.
        return parsed["results"][phase]
    except KeyError:
        print("No phase named: " + phase)
        return None


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
        logger.info("Phase Selected: " + user_phase)
        print(extract_phase(get_solar_data(), phase=user_phase))
        
    except IndexError:
        print("=== Exception loop! ===")
        print(extract_phase(get_solar_data()))
