#encoding=utf-8
__author__ = 'jophyyao'
import os

class Base(object):
    #log path /usr/local/ctier/ctl/var/logs/ctlcenter/{project}/{group}/{job name}
    #         /usr/local/ctier/ctl/var/logs/ctlcenter/{project}/{job name}
    ROOT = "/usr/local/ctier"

    def __init__(self):
        pass

    def create_project(self, project):
        os.system("ctl-project -a create -p %s" % project)

    def create_job(self, file="./job.xml"):
        os.system("ctl-jobs load -f %s" % file)


