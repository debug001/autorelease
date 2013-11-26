#encoding=utf-8
__author__ = 'jophyyao'

from django.conf.urls.defaults import *

urlpatterns = patterns('mail',
    url(r'^release/task/(?P<id>\d+)/(?P<project>\w+)/$', 'release.send'),
)