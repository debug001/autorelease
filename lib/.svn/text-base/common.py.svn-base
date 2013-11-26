#encoding=utf-8
__author__ = 'jophyyao'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import time, os, re

os.environ['DJANGO_SETTINGS_MODULE'] = 'autorelease.settings'
os.environ['LD_LIBRARY_PATH'] = '/usr/local/dev/python/lib'
sys.path.append('/data/python/web/autorelease')


class Common(object):

    def get_return_code(self, url, port):    #url =  www.baidu.com   not http://
        import httplib, socket
        url_result = re.search("^(.+?)(/.*)", url)

        try:
            conn=httplib.HTTPConnection(url_result.group(1), int(port))
            conn.request('GET',url_result.group(2))
        except:
            return 500
        result=conn.getresponse()
        resultStatus=result.status

        return resultStatus

    def validation_url(self, project, env):
        from node import Node
        from common import Common
        from task.models import Validation

        result = {}

        n = Node(project, env)
        ip = []
        for row in n.get():
            if row['hostname'].startswith("Controltier"):
                continue
            ip.append(row['hostname'])

        for vrow in Validation.objects.filter(project=project).values():
            print vrow
            for server in ip:
                if vrow['url'].startswith("ip"):
                    url = re.sub("ip" , server, vrow['url'])
                    return_code = Common().get_return_code(url, vrow['port'])
                    result[url] = return_code

        return result

    def validation_port(self, ip, port):
        import socket

        port = int(port)
        #timeout = 0.2
        #socket.setdefaulttimeout(timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, port))
        except:
            return 1         # can not connect
        else:
            return 0








