#!/usr/bin/python3
"""
Python script that takes in a letter
Sends a POST request to http://0.0.0.0:5000/search_user
With the letter as a parameter
"""

import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": letter}

    res = requests.post(url, data=data)

    try:
        json_res = res.json()
        if json_res:
            print("[{}] {}".format(json_res.get('id'), json_res.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
