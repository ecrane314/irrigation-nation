
"""Get sunset and sunrise time for a lattitude and longitude
For example, 30.267238, -97.755202
Data are provided via API from https://sunrise-sunset.org/api

Evan Crane May 2020
"""

import requests

def get_sunrise_sunset(lat=30.267238, lng=-97.755202, civil=0, nautical=0):
    """Input lattitude and longitude and return sunrise and sunset times"""
    request_mine = "https://sunrise-sunset.org/json?lat=%i&lng=%i" % (lat, lng)
    sunrise, sunset = requests.get(request_mine)
    return 

if __name__ == "__main__":
    get_sunrise_sunset()