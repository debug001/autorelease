#encoding=utf-8
__author__ = 'jophyyao'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from models import Configuration
from user.models import Group, Account
from user.group import get_group_all, get_group_user
from user.manage import get_user_name, get_alluser
from project.models import Node
import re

config = {
    'company' : 'Vipshop',
    'left_workflow_config' : 'active',
    'title_system' : 'active',
    }
js = 'workflow.js'

data = {}


def get_approve_group(project, status):
    group, group_dict = [], {}
    for id in Configuration.objects.filter(project=project, status=status).values()[0]['approve_group'].split(","):
        try:
            group_dict[Group.objects.filter(id=id).values()[0]['name']] = 0
        except ValueError,e:
            group_dict[""] = ""
    for row in group_dict.keys():
        group.append(row)
    return group


@login_required
def list(request, project, status):
    user, email, usernum = request.user.username.split("|")[:]

    if Account.objects.filter(user=user).values()[0]['is_supper_user'] != 1:
        return render_to_response("workflow_error.html", {"config":config})

    data['project'] = project
    data['current_group'] = get_approve_group(project, status)
    data['group'] = []
    for row in get_group_all():
        data['group'].append(row['name'])
    data['status'] = status

    data['user_current'] = []
    data['user'] = []


    #user list ======================================================================
    user_result = {}
    data['user_current_group'] = get_approve_group(project, status)
    for g in data['user_current_group']:
        u_name = get_group_user(g)
        if u_name:
            for username in u_name:
                user_result[username] = 0


    for userid in Configuration.objects.filter(project=project, status=status).values()[0]['approve_user'].strip().split(","):
        if userid:
            user_result[get_user_name(userid)] = 0

    #print user_result

    for username in user_result.keys():
        data['user_current'].append(username)

    for row in get_alluser():
        data['user'].append(row['user'])

    #===============================================================





    if request.method == 'POST':
        result = ""
        print request.POST


        print status



        if request.POST.get('method') == 'group':
            group_list = request.POST.getlist("group_list[]")
            group_dict = {}
            approve_group_id = []
            for g in group_list:
                group_dict[Group.objects.filter(name=g).values()[0]['id']] = 0


            for id in Configuration.objects.filter(status=status, project=project).values()[0]['approve_group'].strip().split(","):
                if id:
                    approve_group_id.append(int(id))

            for row in group_dict.keys():
                if row in approve_group_id:
                    continue
                else:
                    approve_group_id.append(int(row))


            approve_group_id = sorted(approve_group_id)


            for r in approve_group_id:
                result += "%d," % r
            result = re.sub(",$" , "" , result)

            if status == '100':
                Configuration.objects.filter(status=102, project=project).update(approve_group=result)
                Configuration.objects.filter(status=103, project=project).update(approve_group=result)

            Configuration.objects.filter(status=status, project=project).update(approve_group=result)

            return HttpResponseRedirect("/workflow/config/%s/" % project)



        elif request.POST.get('method') == 'user':
            user_list = request.POST.getlist("user_list[]")
            user_dict = {}
            approve_user_id = []
            current_user_id = []
            result = ""
            result_unique = {}

            for u in user_list:
                user_dict[u] = 0

            for appid in Configuration.objects.filter(status=status, project=project).values()[0]['approve_user'].strip().split(","):
                current_user_id.append(appid)

            for user, t in user_dict.iteritems():
                approve_user_id.append(Account.objects.filter(user=user).values()[0]['id'])

            for id in approve_user_id:
                if id in current_user_id:
                    continue
                else:
                    result += "%d," % id

            for o_id in Configuration.objects.filter(status=status, project=project).values()[0]['approve_user'].strip().split(","):
                if o_id:
                    result += "%d," % int(o_id)

            result = re.sub(",$", "", result)

            for r in result.split(","):
                result_unique[r] = 0

            result = ""
            for k,v in result_unique.iteritems():
                result += "%d," % int(k)

            result = re.sub(",$", "", result)

            print result

            if result.split():
                Configuration.objects.filter(status=status, project=project).update(approve_user=result)
                if status == '100':
                    Configuration.objects.filter(status=102, project=project).update(approve_user=result)
                    Configuration.objects.filter(status=103, project=project).update(approve_user=result)

            return HttpResponseRedirect("/workflow/config/%s/" % project)






    return render_to_response("workflow_list.html", {"config":config, "data":data, "js":js})

