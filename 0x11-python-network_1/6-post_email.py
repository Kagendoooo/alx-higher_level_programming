#!/usr/bin/python3
"""
Python script that takes in a URL and an email address
Sends a POST request to the passed URL with the email as a parameter
Finally displays the body of the response
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    res = requests.post(url, data=data)

    print(res.text)
