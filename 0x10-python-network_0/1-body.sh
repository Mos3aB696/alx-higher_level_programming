#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
response=$(curl -s -w "%{http_code}" "$1"); [ "${response: -3}" -eq 200 ] && echo "${response::-3}"
