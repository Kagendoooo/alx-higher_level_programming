#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:School" -d "user_id=98"
