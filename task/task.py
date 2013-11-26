#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Content
from workflow.models import Configuration
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas

config = {
    'company' : 'Vipshop',
    'left_create' : 'active',
    'title_task' : 'active',
}
data = {}

def redirect_validation(request, v, e):
    if not v:
        if e == 'type':
            e = u'类型'.decode("utf-8")
        elif e == 'project':
            e = u'项目名'.decode("utf-8")
        elif e == 'version':
            e = u'版本号'.decode("utf-8")
        elif e == 'comment':
            e = u'上线目的'.decode("utf-8")
        request.session['err'] = u'%s 不能为空'.decode("utf-8") % e
        return 1
    else:
        return 0

def redirect_post_review(sess):
    data['comment'] = sess['comment']
    return HttpResponseRedirect("/task/create/")

def initialization_release_status(project):
    try:
        Configuration.objects.filter(project=project, status=100).values()[0]
    except IndexError, e:
        for n in range(100,106):
            if n == 100:
                st_name = "待上线"
            elif n == 101:
                st_name = "上线中"
            elif n == 102:
                st_name = "上线完成"
            elif n == 103:
                st_name = "上线失败"
            elif n == 104:
                st_name = "回退中"
            elif n == 105:
                st_name = "回退完成"
            elif n == 106:
                st_name = "回退失败"

            cf = Configuration(
                name = st_name,
                project = project,
                status = n,
                approve_user = "",
                approve_group = "",
                mail_to = "",
                mail_cc = "",
                update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time()))),
            )
            cf.save()

    try:
        Configuration.objects.filter(project=project, status=0).values()[0]
    except IndexError, e:
        cf = Configuration(
            name = '取消',
            project = project,
            status = 0,
            approve_user = "",
            approve_group = "",
            update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time()))),
        )
        cf.save()


@login_required
def create(request):
    user, email, usernum = request.user.username.split("|")[:]
    config['user'] = user
    request.session.delete('err')
    if request.session.get('err'):
        config['err'] = request.session.get('err')
    else:
        config['err'] = ''
    return render_to_response("task_create.html", {"config":config})


def create_do(request):
    user, email, usernum = request.user.username.split("|")[:]
    if redirect_validation(request, request.POST['type'], "type"): return redirect_post_review(request.POST)
    if redirect_validation(request, request.POST['project'], "project"): return redirect_post_review(request.POST)
    if redirect_validation(request, request.POST['version'], "version"): return redirect_post_review(request.POST)
    if redirect_validation(request, request.POST['comment'], "comment"): return redirect_post_review(request.POST)

    request.session['err'] = ''
    s = Content(
            type=request.POST['type'],
            project=request.POST['project'],
            env="",
            run_id="",
            comment=request.POST['comment'],
            version=request.POST['version'],
            status = 1,
            create_time = int(time.time()),
            deploy_time = 0,
            finish_time = 0,
            create_user = user,
            deploy_user = "",
    )
    s.save()

    initialization_release_status(request.POST['project'])

    return HttpResponseRedirect("/task/list/1/")









