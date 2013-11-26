#encoding=utf-8
__author__ = 'jophyyao'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import History
import time
from workflow.models import Configuration
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from list import percent_string


config = {
    'company' : 'Vipshop',
    'title_task' : 'active',
}



@login_required
def show(request, project, page_num):
    data={}
    user, email, usernum = request.user.username.split("|")[:]
    config['user'] = user

    page = {}
    page['project'] = project

    page_num = int(page_num)

    limit = 20

    start, end = 0,0

    start = (page_num-1) * limit
    end = start + limit

    if page_num < 2:
        page['last'] = 1
        page['next'] = 1
    else:
        page['last'] = page_num - 1
        page['next'] = page_num + 1

    page_list = {}


    #===================

    count = int(History.objects.filter(project=project).count()/limit)+1
    page_list, page_list_index = {}, 0

    for i in range(1, count+1):
        if page_list_index > 2:
            break
        if i == page_num:
            page_list[i] = "active"
        else:
            page_list[i] = ""
        page_list_index += 1

    if not page_list.has_key(1):
        page_list[1] = "active"

    print page_list



    print start, end
    result = History.objects.filter(project=project).order_by('-finish_time')[start:end]


    tags = 0
    for row in result.values():
        print row
        if row['deploy_time']: row['deploy_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row['deploy_time'])))
        if row['finish_time']: row['finish_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row['finish_time'])))
        data[tags] = {}
        data[tags] = row
        tags += 1



        #status ======================================
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

        #percent
        row['env'] = percent_string(row['env'])


   #print data




    return render_to_response("task_history.html", {"config":config, "data":data, "page":page, "page_list":page_list})
