#!/usr/bin/python3
"""_summary_
    Python script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")
