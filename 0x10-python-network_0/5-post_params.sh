#!/bin/bash
# bash script that takes a URL & sends a POST request to the URL
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
