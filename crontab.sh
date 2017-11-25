#!/bin/bash

echo "* * * * * `which python3` $PWD/timemachine.py --config=$PWD/config.dat --storePath=$PWD >> $PWD/log.txt" | crontab