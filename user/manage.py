#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Account
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas


config = {
    'company' : 'Vipshop',
    'left_user_list' : 'active',
    'title_system' : 'active',
}

def get_user_name(id):
    return Account.objects.filter(id=id).values()[0]['user']

def get_alluser():
    return Account.objects.all().values()

@login_required
def list(request):
    user, email, usernum = request.user.username.split("|")[:]
    config['user'] = user

    data = Account.objects.all().values()

    return render_to_response("user_list.html", {"config":config, "data":data})