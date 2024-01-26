#!/usr/bin/python3
""" The code is importing the `urllib.request` module and the `sys` module.
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
