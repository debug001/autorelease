#encoding=utf-8
__author__ = 'jophyyao'

from django.conf.urls.defaults import *

urlpatterns = patterns('task',
    url(r'^create/$', 'task.create'),
    url(r'^create/do/$', 'task.create_do'),
    url(r'^list/(?P<page_num>\d+)/$', 'list.show'),
    url(r'^view/(?P<id>\d+)/$', 'view.show'),
    url(r'^push/(?P<id>\d+)/(?P<env>\w+)/$', 'push.run'),
    url(r'^approve/(?P<id>\d+)/(?P<type>\d+)/$', 'approve.update'),
    url(r'^rollback/(?P<id>\d+)/$', 'rollback.task'),
    url(r'^history/(?P<project>\w+)/(?P<page_num>\d+)/$', 'history.show'),
    url(r'^validation/url/(?P<project>\w+)/(?P<env>.*)/$', 'validation.url'),
    url(r'percent/100/(?P<id>\d+)/$', 'percent.percent_100'),
)