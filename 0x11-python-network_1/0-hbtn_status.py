#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

response = urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
if __name__ == "__main__":
    with response as res:
        data = res.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {data.decode('utf-8')}")
