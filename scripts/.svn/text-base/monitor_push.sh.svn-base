#!/bin/bash

COUNT=`ps axu |grep -w task_push |grep -v grep |grep -v $0 |wc -l`
if [[ "${COUNT}" == 0 ]]
then
    nohup sh /data/python/web/autorelease/scripts/task_push.sh &
fi