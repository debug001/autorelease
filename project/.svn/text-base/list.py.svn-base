#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db import connection
from models import Node
import time,re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas

config = {
    'company' : 'Vipshop',
    'left_project_list' : 'active',
    'title_env' : 'active',
}

data = {}

@login_required
def show(request):
    user, email, usernum = request.user.username.split("|")[:]
    config['user'] = user
    cursor = connection.cursor()
    sql = "select distinct(project) from project_node"
    cursor.execute(sql)
    rows = cursor.fetchall()
    data['project'] = "["

    for row in rows:
        data['project'] += '"%s",' % row[0]

    data['project'] = re.sub(",$" , "" , data['project'])

    data['project'] += "]"

    project = request.POST.get('project', '')
    if project:
        data['node'] = {}
        data['node'] =  Node.objects.filter(project=project, tags__contains="p").order_by("tags").values()
    else:
        data['node'] = Node.objects.filter(tags__contains="p").order_by("project").values()

    for row in data['node']:
        row['tags'] = re.search("^.*?(p\d+)", row['tags']).group(1)
        row['tags'] = re.sub("^p" , "" , row['tags'])
        row['tags'] = re.sub("$" , "%" , row['tags'])











    return render_to_response("project_list.html", {"config":config, "data" : data})
