#encoding=utf-8
__author__ = 'jophyyao'

import sys, time, os

os.environ['DJANGO_SETTINGS_MODULE'] = 'autorelease.settings'
os.environ['LD_LIBRARY_PATH'] = '/usr/local/dev/python/lib'
sys.path.append('/data/python/web/autorelease')

from tools.mongo import Mongo
from tools.mysql import Mysql
from controltier.log import Log
from mail.release import send
from task.models import Content, History, Rollback

os.putenv('JAVA_HOME', '/usr/local/jdk')
os.putenv('PATH', '/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin:/root/bin:/jre/bin')
os.putenv('CLASSPATH', '/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin:/root/bin:/jre/bin:/lib/tools.jar:/lib/dt.jar')
os.putenv('JETTY_HOME', '/usr/local/ctier/pkgs/jetty-6.1.21')
os.putenv('CTL_BASE', '/usr/local/ctier/ctl/')




id, run_id, project, group, percent, stat = sys.argv[1:]              #stat: u(update)  ro r(rollback)

try:
    int(percent)
except:
    l = Log(project, group, percent)
else:
    l = Log(project, group, "%s%%" % percent)



mysql_conn = Mysql(
    host = '127.0.0.1',
    user = 'root',
    password = 'vipshopmysql',
    database = 'autorelease',
)


mongo_conn = Mongo(
    host = '127.0.0.1',
    database = 'log',
    table = 'log_'+id,
)

mongo_conn.drop()

mongo_conn.insert(
    id = id,
    run_id = run_id,
    content = "",
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
)



while True:

    content = l.load()
    result = os.popen("/usr/local/ctier/pkgs/ctl-3.6.1/bin/ctl-queue").read()

    if run_id in result:
        mongo_conn.update(condition={'id':id}, data={"content":content})
        continue
    else:
        mongo_conn.update(condition={'id':id}, data={"content":content})
        if stat == 'u':
            mysql_conn.save("update task_content set finish_time = '%s', status = '102' where id = '%s'" % (int(time.time()), id))
            time.sleep(10)


            #history
            print "histroy: "
            print id, project, percent

            content_result = Content.objects.filter(id=id, project=project, env=percent).order_by('-finish_time').values()[0]

            h = History(
                task_id = content_result['id'],
                type = content_result['type'],
                project = content_result['project'],
                env = content_result['env'],
                run_id = content_result['run_id'],
                version = content_result['version'],
                status = content_result['status'],
                deploy_time = content_result['deploy_time'],
                finish_time = content_result['finish_time'],
                create_user = content_result['create_user'],
                deploy_user = content_result['deploy_user'],
            )
            h.save()


            mongo_conn.update(
                condition={'task_id':id},
                data={
                    'percent' : 100,
                    'status' : 'success',
                }
            )




            send("", id, project, 102)
        elif stat == 'r':
            mysql_conn.save("update task_content set finish_time = '%s', status = '105' where id = '%s'" % (int(time.time()), id))
            time.sleep(10)

            rollback_history_id = Rollback.objects.filter(task_id=id).order_by('-start_time').values()[0]['id']
            Rollback.objects.filter(id=rollback_history_id, task_id=id).update(finish_time=int(time.time()))
            send("", id, project, 105)
        exit()

    time.sleep(10)







