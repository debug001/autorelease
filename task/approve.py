#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Content, Approve
from workflow.models import Configuration
from user.models import Account, Group
from django.db import connection
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas




def get_approve_user(project, statusid):
    approve_list = []
    approve_dict = {}

    #print statusid

    if statusid > 100:
        statusid = 100

    try:
        Configuration.objects.filter(project=project, status=statusid).values()[0]
    except IndexError, e:
        print "status error"
        return []
    else:

        workflow = Configuration.objects.filter(project=project, status=statusid).values()[0]

    if workflow['approve_group'].strip():
        group = workflow['approve_group'].split(",")
        for userid in group:
            user = Group.objects.filter(id=userid).values()
            for row in user:
                for id in row['userid'].strip().split(","):
                    if id:
                        approve_dict[Account.objects.filter(id=id).values()[0]['user']] = ""

    if workflow['approve_user'].strip():
        group = workflow['approve_user'].split(",")
        for userid in group:
            user = Account.objects.filter(id=userid).values()
            for row in user:
                approve_dict[row['user']] = ""

    #print approve_dict

    for k, v in approve_dict.iteritems():
        approve_list.append(k)

    return approve_list





@login_required
def update(request, id, type):
    user, email, usernum = request.user.username.split("|")[:]
    task = Content.objects.filter(id=id).values()[0]
    approve_list = get_approve_user(task['project'], task['status'])

    if user in approve_list:
        if type == '0':
            status = task['status'] + 1
        else:
            status = 0

        status_str = Configuration.objects.filter(project=task['project'], status=task['status']).values()[0]['name']

        apr = Approve(
            task_id = id,
            approve_name = status_str,
            approve_user = user,
            approve_time = int(time.time()),
            operation = type,

        )
        apr.save()


        try:
            cf = Configuration.objects.filter(status=status, project=task['project']).values()[0]
        except IndexError, e:
            status = 100

        Content.objects.filter(id=id).update(status=status)



    return HttpResponseRedirect("/task/list/1/")

