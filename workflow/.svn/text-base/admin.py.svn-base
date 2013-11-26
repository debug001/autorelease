#encoding=utf-8
__author__ = 'jophyyao'

from models import Configuration
from django.contrib import admin

class Configuration_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project', 'status', 'approve_user', 'approve_group', 'mail_to', 'mail_cc', 'update_time']
    list_display_links = ['id', 'name', 'project', 'status', 'approve_user', 'approve_group', 'mail_to', 'mail_cc', 'update_time']
    search_fields =  ['project']

admin.site.register(Configuration, Configuration_Admin)

