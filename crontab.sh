#!/bin/bash

echo "* * * * * /usr/bin/python3 $PWD/timemachine.py --config=$PWD/config.dat --storePath=$PWD/backup >> $PWD/log.txt 2>&1" | crontab