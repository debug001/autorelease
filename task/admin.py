#encoding=utf-8
__author__ = 'jophyyao'

from models import *
from django.contrib import admin

class Content_Admin(admin.ModelAdmin):
    list_display = ['id','type','project','env', 'run_id', 'comment','version','status', 'create_time','deploy_time','finish_time','create_user','deploy_user']
    list_display_links = ['id','type','project','env', 'run_id', 'comment','version','status', 'create_time','deploy_time','finish_time','create_user','deploy_user']
    search_fields =  ['project']

class Project_Admin(admin.ModelAdmin):
    list_display = ['id','name','group','type', 'ctl_id', 'gradation', 'update_time']
    list_display_links = ['id','name','group','type', 'ctl_id', 'gradation', 'update_time']
    search_fields = ['name']

class History_Admin(admin.ModelAdmin):
    list_display = ['id','task_id', 'type','project','env', 'run_id', 'version','status', 'deploy_time','finish_time','create_user','deploy_user']
    list_display_links = ['id','task_id', 'type','project','env', 'run_id', 'version','status', 'deploy_time','finish_time','create_user','deploy_user']
    search_fields =  ['project']

class Approve_Admin(admin.ModelAdmin):
    list_display = ['id', 'task_id', 'approve_name', 'approve_user', 'approve_time', 'operation']
    list_display_links = ['id', 'task_id', 'approve_name', 'approve_user', 'approve_time', 'operation']
    search_fields =  ['task_id']

class Rollback_Admin(admin.ModelAdmin):
    list_display = ['id', 'task_id', 'start_time', 'finish_time', 'rollback_user']
    list_display_links = ['id', 'task_id', 'start_time', 'finish_time', 'rollback_user']
    search_fields = ['task_id', 'rollback_user']

class Validation_admin(admin.ModelAdmin):
    list_display = ['id', 'project', 'url', 'port']
    list_display_links = ['id', 'project', 'url', 'port']
    search_fields =  ['project']


admin.site.register(Content, Content_Admin)
admin.site.register(Project, Project_Admin)
admin.site.register(History, History_Admin)
admin.site.register(Approve, Approve_Admin)
admin.site.register(Rollback, Rollback_Admin)
admin.site.register(Validation, Validation_admin)
