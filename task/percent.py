#encoding=utf-8
__author__ = 'jophyyao'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from tools.mongo import Mongo

@login_required
def percent_100(request, id):
    mongo_conn = Mongo(
        host = '127.0.0.1',
        database = 'release',
        table = 'percent',
    )

    mongo_conn.update(
        condition={'task_id':id},
        data={
            'percent' : 100,
            'status' : "success"
        }
    )
