#encoding=utf-8
__author__ = 'jophyyao'

from base import Base
import os,re

class Log(Base):
    def __init__(self, project, group, job):
        super(Log, self).__init__()

        self.project = project
        self.group = group
        self.job = job

    def load(self):
        log = os.path.join(self.ROOT, 'ctl/var/logs/ctlcenter', self.project, self.group, self.job)
        #print log
        content = {}

        for file in os.listdir(log):
            os.chdir(log)
            content[file] = int(os.stat(file).st_ctime)

        for row in sorted(content.iteritems(), key=lambda d:d[1], reverse = False ):
            #print row
            pass

        #print row[0]
        rows = ""

        for row in open(row[0], "r"):
            row = re.sub("\n" ,"<br>" , row)
            rows += row

        return rows






