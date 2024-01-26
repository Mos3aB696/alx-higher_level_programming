#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


import requests
if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    data = response.content
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data.decode('utf-8')}")
