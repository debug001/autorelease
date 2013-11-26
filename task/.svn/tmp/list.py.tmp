#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Content, Project
from workflow.models import Configuration
from django.db import connection
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from approve import get_approve_user
from lib.percent import Percent


config = {
    'company' : 'Vipshop',
    'left_list' : 'active',
    'title_task' : 'active',
}


def percent_string(percent):
    try:
        int(percent)
    except:
        return percent
    else:
        return "%s%%" % percent

@login_required
def show(request,page_num):
    user, email, usernum = request.user.username.split("|")[:]
    config['user'] = user
    count = 0
    cursor = connection.cursor()
    sql = "select count(id) from task_content"
    cursor.execute(sql)
    row = cursor.fetchone()

    limit = 15
    if not page_num:
        page_num = 1
    else:
        page_num = int(page_num)
    start, end = 0,0

    start = (page_num-1) * limit
    end = start + limit


    count = int(row[0]/limit)+1
    next = page_num+1

    if page_num < 2:
        page_num = 1
        last = page_num
        next = 1
    else:
        last = page_num-1

    id = 0

    if end > row[0]:
        end = row[0]
    #print start, end
    data = {}
    percent_id_list = []


    result = Content.objects.order_by('-id')[start:end]
    result = result.values()
    for row in result:
        percent_id_list.append(row['id'])
        if row['create_time']: row['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row['create_time'])))
        if row['deploy_time']: row['deploy_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row['deploy_time'])))
        if row['finish_time']: row['finish_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row['finish_time'])))


        if row['status'] > 100:
            p = Percent(int(row['id']), row['project'], row['project'], str(row['env']))
            p.analyze()


        #print row['status']

        cf_status_list = []
        for cf in Configuration.objects.filter(project=row['project']).values():
            if cf['status'] < 100:
                cf_status_list.append(cf['status'])

        if row['status'] < 100 and row['status'] not in cf_status_list:
            row['status'] = 100

        try:
            status_str = Configuration.objects.filter(project=row['project'], status=row['status']).values()[0]['name']
        except IndexError, e:
            status_str = "status error: %s" % row['status']

        if 0 < row['status'] < 100:
            row['status_str'] = u"待%s审批" % status_str
        else:
            row['status_str'] = status_str
        #row['status_str'] = ""
        row['status_str'].encode('utf-8')


        #print row['project'], row['status']

        approve_user = get_approve_user(row['project'], row['status'])

        #print row['id'],user,approve_user

        row['deploy_approve'] = 0

        if user in approve_user:
            row['approve'] = 1
        else:
            row['approve'] = 0

        #print row['id'],row['status'],row['approve']
        if row['status'] >= 100:
            #added deploy limit
            if row['approve'] == 1:
                row['deploy_approve'] = 1
            else:
                row['deploy_approve'] = 0

        #print row['id'], row['approve'], row['deploy_approve']



        #percent query
        row['percent'] = {}
        for pj in Project.objects.filter(name=row['project'], type=row['type']).order_by('gradation').values():
            row['percent'][pj['gradation']] = percent_string(pj['gradation'])

        row['env'] = percent_string(row['env'])




        data[id] = {}
        data[id] = row
        id += 1


    #print data
    page_list, page_list_index = {}, 0

    for i in range(1, count+1):
        if page_list_index > 6:
            break
        if i == page_num:
            page_list[i] = "active"
        else:
            page_list[i] = ""
        page_list_index += 1
    #print page_list

    if not page_list.has_key(1):
        page_list[1] = "active"

    #print page_list, count







    return render_to_response("task_list.html", {
        "config":config, "data":data, "next":next, "last":last, "page_list":page_list, "percent_id_list":percent_id_list,
    })
