#encoding=utf-8
__author__ = 'jophyyao'

from django.db import models

class Configuration(models.Model):
    name = models.CharField(max_length=30)
    project = models.CharField(max_length=30)
    status = models.IntegerField()
    approve_user = models.CharField(max_length=100, null=True)
    approve_group = models.CharField(max_length=100, null=True)
    mail_to = models.CharField(max_length=1000, null=True)
    mail_cc = models.CharField(max_length=1000, null=True)
    update_time = models.DateTimeField(auto_now=False, auto_now_add=False)











