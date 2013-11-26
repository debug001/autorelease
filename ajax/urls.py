#encoding=utf-8
__author__ = 'jophyyao'

from django.conf.urls.defaults import *

urlpatterns = patterns('ajax',
    url(r'^get_project/$', 'get_project.index'),
    url(r'^get_current_user/$', 'get_current_user.index'),
    url(r'^current_user_add/$', 'get_current_user.current_user_add'),
    url(r'^get_user/$', 'get_current_user.get_user'),
    url(r'^unique_group_add/$', 'get_current_user.unique_group_add'),
    url(r'^unique_user_add/$', 'get_current_user.unique_user_add'),
    url(r'^get_percent/list/(?P<id>\d+)/$', 'get_percent.list'),
    url(r'^get_percent/get_id/$', 'get_percent.get_id'),
)