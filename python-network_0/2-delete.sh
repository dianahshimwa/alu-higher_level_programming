#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of the resposne
curl -sX DELETE "$1"
