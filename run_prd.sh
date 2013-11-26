#!/bin/bash

ps axu |grep uwsgi |grep release |grep -v grep |grep -v $0 |awk '{print $2}' |xargs kill -9
sleep 3
uwsgi -M -x django.xml  -d /tmp/release.log
