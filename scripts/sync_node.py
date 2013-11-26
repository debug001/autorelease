#encoding=utf-8
__author__ = 'jophyyao'

import sys, os, time, re

sys.path.insert(0, '../')
from controltier.node import Node
from tools.mysql import Mysql

mysql_conn = Mysql(
    host = '127.0.0.1',
    user = 'root',
    password = 'vipshopmysql',
    database = 'autorelease',
    )

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))

for project in os.listdir('/usr/local/ctier/ctl/projects'):
     n = Node(project)
     for k, v in n.analysis().iteritems():
         result = mysql_conn.fetch("select count(id) from project_node where project = '%s' and hostname = '%s'" % (project, v['hostname']))
         if result['count(id)']:
             mysql_conn.save("""
             update project_node set
             name = '{name}',
             description = '{description}',
             tags = '{tags}',
             ctlusername = '{ctlusername}',
             osfamily = '{osfamily}',
             osname = '{osname}',
             osarch = '{osarch}',
             osversion = '{osversion}',
             updatetime = '{updatetime}'
             where project = '{project}' and hostname = '{hostname}'
             """.format(
                 project = project,
                 name = v['name'],
                 description = v['description'],
                 tags = v['tags'],
                 ctlusername = v['ctlUsername'],
                 osfamily = v['osFamily'],
                 osname = v['osName'],
                 osarch = v['osArch'],
                 osversion = v['osVersion'],
                 hostname = v['hostname'],
                 updatetime = now,
             )
             )
         else:
             mysql_conn.save("""
             insert into project_node ()values(
             NULL, '{project}', '{name}', '{description}', '{tags}', '{ctlusername}', '{osfamily}', '{osname}', '{osarch}', '{osversion}',
              '{hostname}', '{updatetime}')
             """.format(
                 project = project,
                 name = v['name'],
                 description = v['description'],
                 tags = v['tags'],
                 ctlusername = v['ctlUsername'],
                 osfamily = v['osFamily'],
                 osname = v['osName'],
                 osarch = v['osArch'],
                 osversion = v['osVersion'],
                 hostname = v['hostname'],
                 updatetime = now,
             )
             )




