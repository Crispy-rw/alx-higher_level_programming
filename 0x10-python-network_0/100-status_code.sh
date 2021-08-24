#!/bin/bash
# Takes a URL and sends a request to it and displays the status code of the response
curl -s -w "%{http_code}" "$1" -o /dev/null
