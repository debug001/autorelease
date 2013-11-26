#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Content, Approve
import time, re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from list import percent_string

config = {
    'company' : 'Vipshop',
}

@login_required
def show(request, id):
    user, email, usernum = request.user.username.split("|")[:]
    config['user'] = user

    result = Content.objects.filter(id=id)
    result = result.values()
    for row in result:
        if row['create_time']: row['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row['create_time'])))
        if row['deploy_time']: row['deploy_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row['deploy_time'])))
        if row['finish_time']: row['finish_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row['finish_time'])))
        row['comment'] = re.sub("\r\n", "<br>", row['comment'])
        row['env'] = percent_string(row['env'])

    approve_data = {}
    index = 1
    for apv in Approve.objects.filter(task_id=id).values():
        if apv['approve_time']: apv['approve_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(apv['approve_time'])))
        if apv['operation'] == 0:
            apv['operation'] = ''
        else:
            apv['operation'] = '审批退回'
        approve_data[index] = apv
        index +=1



    print approve_data

    return render_to_response("task_view.html", {"config":config, "data":row, "approve":approve_data})
