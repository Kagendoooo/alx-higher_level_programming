#!/usr/bin/python3
"""
Python script that takes in a URL and an email
Sends a POST request to the passed URL with the email as a parameter
Displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        b = response.read()
        print(b.decode('utf-8'))
