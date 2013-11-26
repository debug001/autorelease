#encoding=utf-8
__author__ = 'jophyyao'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Account, Group
import time,re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from manage import get_user_name


config = {
    'company' : 'Vipshop',
    'left_group_list' : 'active',
    'title_system' : 'active',
}
js = 'group.js'

data = {}

def get_group_all():
    return Group.objects.all().values()

def get_group_name(id):
    return Group.objects.filter(id=id).values()[0]['name']

def get_group_user_name_id(id):            #name : userid
    result = {}
    for id in Group.objects.filter(id=id).values()[0]['userid'].strip().split(","):
        if id:
            result[Account.objects.filter(id=id).values()[0]['user']] = id

    return result

def get_group_user(name):
    if name:
        result = {}
        for userid in Group.objects.filter(name=name).values()[0]['userid'].strip().split(","):
            if userid:
                username = Account.objects.filter(id=userid).values()[0]['user']
                if username:
                    result[username] = 0
        return result




@login_required
def list(request):
    user, email, usernum = request.user.username.split("|")[:]
    config['user'] = user

    print request.POST

    data['group'] = {}

    for row in Group.objects.all().order_by('-id').values():
        data['group'][row['name']] = row['id']

    data['user'] = {}
    for row in Account.objects.all().order_by('-user').values():
        data['user'][row['user']] = row['id']

    group_list = {}

    if request.method == 'POST':
        groupid=request.POST.get('group', '')
        userlist=request.POST.getlist('user[]', '')

        userid_str = ""
        user_id = []

        for id in Group.objects.filter(id=groupid).values()[0]['userid'].strip().split(","):
            if id:
                user_id.append(int(id))

        for u in userlist:
            uid = Account.objects.filter(user=u).values()[0]['id']
            if uid in user_id:
                continue
            else:
                user_id.append(int(uid))

        user_id = sorted(user_id)


        for row in user_id:
            userid_str += "%d," % row
        userid_str = re.sub(",$", "", userid_str)

        Group.objects.filter(id=groupid).update(userid=userid_str)



    tags = 1
    for row in get_group_all():
        group_list[tags] = {}
        group_list[tags]['userid'] = ""

        for id in row['userid'].strip().split(","):
            if id:
                group_list[tags]['userid'] += "%s<br>" % get_user_name(id)


        group_list[tags]['name'] = row['name']
        tags += 1

    print group_list



    return render_to_response("group_list.html", {"config":config, "data":data, "js":js, "group_list":group_list})