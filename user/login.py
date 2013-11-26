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

@login_required
def index(request):
    user, email, usernum = request.user.username.split("|")[:]
    result = Account.objects.filter(user=user).count()

    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))

    if result:
        Account.objects.filter(user=user).update(last_login_time=now)
    else:
        a = Account(
            user = user,
            email = email,
            usernum = usernum,
            is_supper_user = 0,
            last_login_time = now,
        )
        a.save()
    Account.objects.filter(user=user).update(usernum=usernum, last_login_time=now)
    return HttpResponseRedirect("/task/list/1/")
