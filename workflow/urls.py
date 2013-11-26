#encoding=utf-8
__author__ = 'jophyyao'

from django.conf.urls.defaults import *

urlpatterns = patterns('workflow',
    url(r'^config/$', 'workflow.configuration'),
    url(r'^config/(?P<pjt>\w+)/$', 'workflow.configuration'),
    url(r'^approve/(?P<project>\w+)/(?P<status>\d+)/$', 'approve.list'),
)