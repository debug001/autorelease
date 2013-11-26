#encoding=utf-8
__author__ = 'jophyyao'

from django.db import models

class Account(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    usernum = models.CharField(max_length=30)
    is_supper_user = models.IntegerField()
    last_login_time = models.DateTimeField(auto_now=False, auto_now_add=False)

class Group(models.Model):
    name = models.CharField(max_length=50)
    userid = models.CharField(max_length=200)
    update_time = models.DateTimeField(auto_now=False, auto_now_add=False)








