#!/usr/bin/python3

"""
    The code is importing the necessary modules (`requests` and `sys`)
    and the `HTTPBasicAuth` class
    from the `requests.auth` module.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    response = requests.get('https://api.github.com/user', auth=auth)
    print(response.json().get('id'))
