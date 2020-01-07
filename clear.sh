#!/bin/bash
for pid in $(ps -C "python3 ConcurrentTimeSizeRotateLogHandler_test.py" -o pid=)
do
    echo $pid
    sudo kill -9 $pid
done
