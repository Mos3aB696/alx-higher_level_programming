#!/usr/bin/python3
"""_summary_
    Python script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""


import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = urllib.request.urlopen(url)
        with response as res:
            print(res.read().decode('utf-8'))

    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
