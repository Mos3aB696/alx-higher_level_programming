#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


import requests
if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    data = response.content.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
