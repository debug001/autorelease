#encoding=utf-8
__author__ = 'jophyyao'

from django.db import models

class Content(models.Model):
    type = models.CharField(max_length=20)
    project = models.CharField(max_length=30)
    env = models.CharField(max_length=20)
    run_id = models.CharField(max_length=20)
    comment = models.TextField()
    version = models.CharField(max_length=80)
    status = models.IntegerField()
    create_time = models.IntegerField()
    deploy_time = models.IntegerField()
    finish_time = models.IntegerField()
    create_user = models.CharField(max_length=30)
    deploy_user = models.CharField(max_length=30)

class Project(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    group = models.CharField(max_length=30)
    ctl_id = models.IntegerField()
    gradation = models.CharField(max_length=30)
    update_time = models.DateTimeField(auto_now=False, auto_now_add=False)

class History(models.Model):
    task_id = models.IntegerField()
    type = models.CharField(max_length=20)
    project = models.CharField(max_length=30)
    env = models.CharField(max_length=20)
    run_id = models.CharField(max_length=20)
    version = models.CharField(max_length=80)
    status = models.IntegerField()
    deploy_time = models.IntegerField()
    finish_time = models.IntegerField()
    create_user = models.CharField(max_length=30)
    deploy_user = models.CharField(max_length=30)

class Approve(models.Model):
    task_id = models.IntegerField()
    approve_name = models.CharField(max_length=30)
    approve_user = models.CharField(max_length=50)
    approve_time = models.IntegerField()
    operation = models.IntegerField()

class Rollback(models.Model):
    task_id = models.IntegerField()
    start_time = models.IntegerField(null=True)
    finish_time = models.IntegerField(null=True)
    rollback_user = models.CharField(max_length=30, null=True)

class Validation(models.Model):
    project = models.CharField(max_length=30)
    url= models.CharField(max_length=50)
    port = models.IntegerField(null=True)















