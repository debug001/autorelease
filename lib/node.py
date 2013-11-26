#encoding=utf-8
__author__ = 'jophyyao'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import time, os

os.environ['DJANGO_SETTINGS_MODULE'] = 'autorelease.settings'
os.environ['LD_LIBRARY_PATH'] = '/usr/local/dev/python/lib'
sys.path.append('/data/python/web/autorelease')
from project.models import Node as Tnode


class Node(object):

    def __init__(self, project, env=""):
        self.project = project
        self.env = env

    def get(self):
        try:
            int(self.env)
        except ValueError:
            self.env = ""
        else:
            self.env = "p%s" % self.env

        result = Tnode.objects.filter(project=self.project).exclude(hostname="Controltier-101-61").order_by('hostname').values()


        return result

