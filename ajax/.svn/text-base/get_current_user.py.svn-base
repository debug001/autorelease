#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse
from user.models import Account, Group
from workflow.models import Configuration
import re

def index(request):
    response=HttpResponse()
    #response['Content-Type']="text/javascript"
    group=request.POST.get('group[]', '')

    ret=""
    result=""

    dt = {}

    uid = {}

    if group:
        for row in Group.objects.filter(id=group).values():
            for i in row['userid'].split(','):
                uid[i] = 0

        for id in uid.keys():
            u = Account.objects.filter(id=id).values()[0]
            result += u['user']+"|"
            dt[row['name']] = 0
    else:
        result="error"


    response.write(result)
    return response


def current_user_add(request):
    response=HttpResponse()
    groupid=request.POST.get('groupid[]', '')
    user=request.POST.getlist('user[]', '')

    result = ""
    udict = {}

    if user:
        for u in user:
            userid = Account.objects.filter(user=u).values()[0]['id']
            udict[userid] = u

        for id in Group.objects.filter(id=groupid).values()[0]['userid'].strip().split(","):
            if not id:
                break
            if int(id) in udict.keys():
                del(udict[int(id)])

        for row in udict:
            result += udict[row]+"|"
    else:
        result="error"

    response.write(result)
    return response


def get_user(request):
    response=HttpResponse()
    group_name=request.POST.get('group[]', '')
    user_dict = {}
    result = ""
    for id in Group.objects.filter(name=group_name).values()[0]['userid'].split(","):
        user_dict[Account.objects.filter(id=id).values()[0]['user']] = 0

    for name in user_dict.keys():
        result += name+"|"


    response.write(result)
    return response


def unique_group_add(request):
    response=HttpResponse()
    group_list=request.POST.getlist('group_list[]', '')
    status=request.POST.get('status', '')
    project=request.POST.get('project', '')
    current_group = {}
    result = ""


    approve_group = Configuration.objects.filter(project=project, status=status).values()[0]['approve_group']

    if not approve_group.strip():
        for g in group_list:
            result += g+"|"

        #print result
        response.write(result)
        return response


    for id in approve_group.split(","):
        current_group[Group.objects.filter(id=id).values()[0]['name']] = 0

    for cg in group_list:
        if cg in current_group.keys():
            continue
        else:
            result += cg+"|"

    #print result

    response.write(result)
    return response







def unique_user_add(request):
    response=HttpResponse()
    user_list=request.POST.getlist('user_list[]', '')
    status=request.POST.get('status', '')
    project=request.POST.get('project', '')
    current_user = {}
    result = ""


    approve_user = Configuration.objects.filter(project=project, status=status).values()[0]['approve_user']
    if approve_user.strip():
        approve_user = re.sub(",$" , "" , approve_user)
        approve_user += ","
    #approve_user += Configuration.objects.filter(project=project, status=status).values()[0]['approve_group']

    if not approve_user.strip():
        for g in user_list:
            result += g+"|"

        #print result
        response.write(result)
        return response

    print approve_user
    for id in approve_user.split(","):
        if id:
            current_user[Account.objects.filter(id=int(id)).values()[0]['user']] = 0

    for cg in user_list:
        if cg in current_user.keys():
            continue
        else:
            result += cg+"|"

    print result

    response.write(result)
    return response











