#encoding=utf-8
__author__ = 'jophyyao'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import History, Project, Content, Rollback
import time, os, re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from mail.release import send

@login_required
def task(request, id):
    user, email, usernum = request.user.username.split("|")[:]
    ROOT = os.path.abspath(os.path.dirname(__file__))

    content_result = Content.objects.filter(id=id).values()[0]

    history_result = History.objects.filter(project=content_result['project'], env=content_result['env']).order_by('-finish_time').values()[1]

    project_result = Project.objects.filter(
        name = history_result['project'],
        type = history_result['type'],
        gradation = history_result['env'],
    ).values()[0]

    send(request, id, history_result['project'], 104)
    Content.objects.filter(id=id).update(status=104)
    r = Rollback(
        task_id = id,
        start_time = int(time.time()),
        finish_time = None,
        rollback_user = user,
    )
    r.save()



    print project_result['ctl_id'], history_result['version'], history_result['run_id']
    print "source /root/.bash_profile; /usr/local/ctier/pkgs/ctl-3.6.1/bin/ctl-run -i %d -- -Version %s" % (project_result['ctl_id'], history_result['version'])

    result = os.popen("source /root/.bash_profile; /usr/local/ctier/pkgs/ctl-3.6.1/bin/ctl-run -i %d -- -Version %s" % (project_result['ctl_id'], history_result['version']))

    os.system("python %s/../scripts/log_tail.py %s %s %s %s %s r &" % (ROOT, id, history_result['run_id'], history_result['project'], history_result['project'], history_result['env']))






    return HttpResponseRedirect("/task/view/%s/" % id)
