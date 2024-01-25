#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
curl -s http://$1 | grep -oP '(?<=<body>).*?(?=</body>)'
