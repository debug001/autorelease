#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from models import Configuration
from project.models import Node
from user.group import get_group_name, get_group_user_name_id
from user.manage import get_user_name
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


config = {
    'company' : 'Vipshop',
    'left_workflow_config' : 'active',
    'title_system' : 'active',
}

data = {}


def get_mail_address(project, status):
    result = {}
    result['to'] = []
    result['cc'] = []
    for row in Configuration.objects.filter(project=project, status=status).values():
        if row['mail_to'].strip():
            for to_user in row['mail_to'].strip().split(","):
                if to_user and to_user not in result['to']:
                    result['to'].append("%s@vipshop.com" % to_user)

            for cc_user in row['mail_cc'].strip().split(","):
                if cc_user and cc_user not in result['cc']:
                    result['cc'].append("%s@vipshop.com" % cc_user)

    return result

def get_status_name(project, status):
    return Configuration.objects.filter(project=project, status=status).values()[0]['name']



@login_required
def configuration(request, pjt=""):
    user, email, usernum = request.user.username.split("|")[:]
    config['user'] = user

    unique = {}

    data['project'] = "["


    for row in Node.objects.all().values():
        if unique.has_key(row['project']):
            continue
        unique[row['project']] = ""
        data['project'] += '"%s",' % row['project']

    data['project'] = re.sub(",$" , "" , data['project'])
    data['project'] += "]"



    project = ""
    project = request.POST.get('project', '')


    if pjt != '':
        project = pjt

    contents = {}
    result_table = {}
    unique_user_name = {}
    if project:
        index = 1
        index_table = 1
        for row in Configuration.objects.filter(project=project).order_by('status').values():
            if index == 1:
                row['name'] = u"新建"
                contents[index] = {}
                contents[index][row['name']] = 1000
                index += 1
                continue
            if row['status'] == 0 or row['status'] == 102 or row['status'] == 103 or row['status'] > 103:
                continue
            if row['status'] > 0 and row['status'] < 100:
                row['name'] += u"审批"
            contents[index] = {}
            contents[index][row['name']] = row['status']
            index += 1

        #table

        for row in Configuration.objects.filter(project=project).order_by('status').values():
            if row['status'] > 0 and row['status'] < 101:
                unique_user_name = {}
                result_table[index_table] = {}
                result_table[index_table]['approve_group'] = ""
                result_table[index_table]['approve_user'] = ""
                for id in row['approve_group'].strip().split(","):
                    if id:
                        result_table[index_table]['approve_group'] += "%s<br>" % get_group_name(id)

                        for name, id in get_group_user_name_id(id).iteritems():
                            unique_user_name[name] = 0
                #print unique_user_name



                for id in row['approve_user'].strip().split(","):
                    if id:
                        unique_user_name[get_user_name(id)] = 0

                for user in unique_user_name.keys():
                    result_table[index_table]['approve_user'] += "%s<br>" % user






                result_table[index_table]['name'] = row['name']
                result_table[index_table]['project'] = row['project']
                result_table[index_table]['status'] = row['status']
                index_table += 1

    else:
        pass


    #print contents
    #print result_table






    return render_to_response("sys_workflow_view.html", {"config":config, "data":data, "contents":contents, "project":project, "result_table" : result_table })


