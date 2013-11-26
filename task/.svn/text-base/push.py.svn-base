#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db import connection
from models import Content
import subprocess, time, os, re, sys
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from mail.release import send
import subprocess
sys.path.append('/data/python/web/autorelease')
from tools.daemon import Daemon
from tools.mongo import Mongo





def ctl_log_query(i, q, ROOT, id, run_id, project, group, percent):
    while True:
        subprocess.call(
            "python %s/../scripts/log_tail.py %s %s %s %s %s u" % (ROOT, id, run_id, project, group, percent),
            shell=True,
            stdout=open('/dev/null', 'w'),
            stderr=subprocess.STDOUT
        )
        q.task_done()





@login_required
def run(request, id, env):              #env == percent
    print id,env
    user, email, usernum = request.user.username.split("|")[:]
    Content.objects.filter(id=id).update(env=env)
    ROOT = os.path.abspath(os.path.dirname(__file__))

    version, ctl_id = "", 0
    cursor = connection.cursor()
    sql = """
    select tc.version, tp.ctl_id from task_content tc left join task_project tp on tc.project = tp.name where tc.id = '%s' and tp.gradation = '%s';
    """ % (id, env)
    cursor.execute(sql)
    row = cursor.fetchone()
    version, ctl_id = row[0:]

    #result = subprocess.call("ctl-run -i %d -- -Version %s" % (ctl_id, version), shell=True, stderr=subprocess.STDOUT)
    result = os.popen("source /root/.bash_profile; /usr/local/ctier/pkgs/ctl-3.6.1/bin/ctl-run -i %d -- -Version %s" % (ctl_id, version))

    #update or insert case status
    mongo_conn = Mongo(
        host = '127.0.0.1',
        database = 'release',
        table = 'percent',
    )

    mongo_conn.remove(
        task_id = int(id)
    )

    mongo_conn.insert(
        task_id = int(id),
        status = 'running',
        percent = 1
    )


    cursor = connection.cursor()
    sql = """
    select tp.name, tp.group, tp.gradation, tc.status from task_content tc
    left join task_project tp
    on  tc.project = tp.name and tc.env = tp.gradation
    where tc.id = '%s'
    """ % id
    cursor.execute(sql)
    row = cursor.fetchone()

    project, group, percent, status = row[0], row[1], row[2], row[3]


    run_id = ""
    print result
    for i in result:
        if re.search("^\[(\d+)\].*", i):
            run_id = re.search("^\[(\d+)\].*", i).group(1)



    print run_id



    Content.objects.filter(id=id).update(
        run_id=run_id,
        deploy_time = int(time.time()),
        deploy_user = user,
        status = 101,
    )
    send(request, id, project, 101)

    print "nohup /usr/bin/python /data/python/web/autorelease/scripts/log_tail.py %s %s %s %s %s u >> /tmp/run.log &\n" % (id, run_id, project, group, percent)

    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))

    cmd = "nohup /usr/bin/python /data/python/web/autorelease/scripts/log_tail.py %s %s %s %s %s u >> /tmp/run.log &\n" % (id, run_id, project, group, percent)



    f = open("/tmp/task", "a")
    f.write(cmd)
    f.close()














#    subprocess.call(
#        "nohup python %s/../scripts/log_tail.py %s %s %s %s %s u >/dev/null 2>&1 &" % (ROOT, id, run_id, project, group, percent),
#        shell=True,
#        stdout=open('/dev/null', 'w'),
#        stderr=subprocess.STDOUT
#    )

    #os.system("nohup python %s/../scripts/log_tail.py %s %s %s %s %s u >/dev/null 2>&1 &" % (ROOT, id, run_id, project, group, percent))




    return HttpResponseRedirect("/task/view/%s?m=1&p=%s" % (id, project))


