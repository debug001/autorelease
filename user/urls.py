#encoding=utf-8
__author__ = 'jophyyao'

from django.conf.urls.defaults import *

urlpatterns = patterns('user',
    url(r'^$', 'login.index'),
    url(r'^login/$', 'login.index'),
    url(r'^list/$', 'manage.list'),
    url(r'^group/$', 'group.list'),
)
