#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a Strategy Name to run"
    exit 1
fi

pdm run freqtrade trade --logfile user_data/logs/log_$1.log --db-url sqlite:///user_data/db/db_$1.sqlite --strategy $1 --config user_data/configs/config_$1.json