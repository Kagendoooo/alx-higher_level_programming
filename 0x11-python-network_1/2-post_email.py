#!/usr/bin/python3
"""
Python script that takes in a URL and an email
Sends a POST request to the passed URL with the email as a parameter
Displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data) as response:
    body = response.read()

print(body.decode('utf-8'))
