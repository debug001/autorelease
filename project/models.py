#encoding=utf-8
__author__ = 'jophyyao'

from django.db import models

class Node(models.Model):
    project = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.CharField(max_length=30)
    ctlusername = models.CharField(max_length=30)
    osfamily = models.CharField(max_length=30)
    osname = models.CharField(max_length=30)
    osarch = models.CharField(max_length=30)
    osversion = models.CharField(max_length=30)
    hostname = models.CharField(max_length=50)
    updatetime =  models.DateTimeField(auto_now=False, auto_now_add=False)








