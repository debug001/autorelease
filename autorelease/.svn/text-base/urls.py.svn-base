from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^task/', include('task.urls')),
    url(r'^ajax/', include('ajax.urls')),
    url(r'^log/', include('log.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^workflow/', include('workflow.urls')),
    url(r'^mail/', include('mail.urls')),
    url(r'^login/$', 'django_cas.views.login'),
    url(r'^logout/$', 'django_cas.views.logout'),
    url(r'^$', include('user.urls')),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR+"/css"}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR+"/js"}),

)
