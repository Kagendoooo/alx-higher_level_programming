#!/usr/bin/python3
"""
Python script that takes in a URL
Sends a request to the URL
Displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    print(res.headers.get('X-Request-Id'))
