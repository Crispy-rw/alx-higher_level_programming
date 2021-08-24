#!/bin/bash
# Takes in a URL and sends a request to it and displays the response message You got me!
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
