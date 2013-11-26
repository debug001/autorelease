#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from task.models import Project
from controltier.log import Log
from django.db import connection
from tools.mongo import Mongo
import time

config = {
    'company' : 'Vipshop',
}




def load_file(request, id):
    cursor = connection.cursor()
    sql = """
    select tp.name, tp.group, tp.gradation from task_content tc
    left join task_project tp
    on  tc.project = tp.name and tc.env = tp.gradation
    where tc.id = '%s'
    """ % id
    cursor.execute(sql)
    row = cursor.fetchone()

    project, group, percent = row[0], row[1], row[2]

    #print project, group, percent

    l = Log(project, group, "%d%%" % percent)
    content = l.load()

    return render_to_response("log_view.html", {"config":config, "content":content})


def load(request, id):
    cursor = connection.cursor()
    sql = """
        select tp.name, tp.group, tp.gradation from task_content tc
        left join task_project tp
        on  tc.project = tp.name and tc.env = tp.gradation
        where tc.id = '%s'
        """ % id
    cursor.execute(sql)
    row = cursor.fetchone()

    project, group, percent = row[0], row[1], row[2]

    #print project, group, percent



    log_mongo = ""

    mongo_conn = Mongo(
        host = '127.0.0.1',
        database = 'log',
        table = 'log_'+id,
    )

    log_mongo = mongo_conn.find()

    contents = ""
    for row in log_mongo:
        contents += row['content']

    return render_to_response("log_view.html", {"config":config, "content":contents})









