#!/bin/bash

mv /tmp/release.log /apps/logs/release/release_`date +%Y%m%d`.log
ps axu |grep task_push |grep -v grep |grep -v $0 |awk '{print $2}' |xargs kill -9
cd /data/python/web/autorelease
sh /data/python/web/autorelease/run_prd.sh
