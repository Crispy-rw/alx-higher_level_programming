#!/bin/bash
# Display the size of the body of a request
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
