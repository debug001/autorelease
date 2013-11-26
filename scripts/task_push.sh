#!/bin/bash

FILE="/tmp/task"


while true
do
    line=`wc -l ${FILE} |awk '{print $1}'`
    if [[ "${line}" > 0 ]]
    then
        /bin/sh ${FILE}
        > /tmp/task
    fi
    sleep 10
done