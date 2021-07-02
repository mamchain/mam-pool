#!/bin/bash

while true
do
    ss -lnt | grep 7702
    if [ $? -eq 0 ];then
        python3 init.py
        node init.js
    else
        sleep 1
        echo "..."
    fi
done