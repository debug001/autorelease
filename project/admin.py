#encoding=utf-8
__author__ = 'jophyyao'

from models import Node
from django.contrib import admin

class Node_Admin(admin.ModelAdmin):
    list_display = ['id','project','name','description', 'tags', 'ctlusername','osfamily','osname','osarch','osversion','hostname','updatetime']
    list_display_links = ['id','project','name','description', 'tags', 'ctlusername','osfamily','osname','osarch','osversion','hostname','updatetime']
    search_fields = ['project']

admin.site.register(Node, Node_Admin)

