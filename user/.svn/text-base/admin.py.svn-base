#encoding=utf-8
__author__ = 'jophyyao'

from models import Account, Group
from django.contrib import admin

class Account_Admin(admin.ModelAdmin):
    list_display = ['id','user','email','usernum', 'is_supper_user', 'last_login_time']
    list_display_links = ['id','user','email','usernum', 'is_supper_user', 'last_login_time']
    search_fields =  ['user']

class Group_Admin(admin.ModelAdmin):
    list_display = ['id','name','userid','update_time']
    list_display_links = ['id','name','userid','update_time']
    search_fields =  ['name']

admin.site.register(Account, Account_Admin)
admin.site.register(Group, Group_Admin)

