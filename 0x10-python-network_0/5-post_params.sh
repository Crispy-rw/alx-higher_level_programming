#!/bin/bash
# Sends a POST request to the passed URL, and displays the body of the response
curl -sX POST "$1" --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"
