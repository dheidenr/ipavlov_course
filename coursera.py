

# freegeoip.net/json
# python 3 -m venv env
import requests
import pprint
import sys
import os


def get_location_info():
    return requests.get("http://ip-api.com/json/").json()


if __name__ == "__main__":
    pprint.pprint(get_location_info())
    print(bool(0.000001))
    print(sys.path)
