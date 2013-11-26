#encoding=utf-8
__author__ = 'jophyyao'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from django.http import HttpResponse
from task.models import Content
from tools.mongo import Mongo
from lib.percent import Percent
import re


def get_id(request):
    response=HttpResponse()
    result = ""
    for row in Content.objects.all().values():
        result += "%d|" % row['id']

    result = re.sub("|$" , "" , result)

    response.write(result)
    return response





def list(request, id):
    result = ""

    id = int(id)

    mongo_conn = Mongo(
        host = '127.0.0.1',
        database = 'release',
        table = 'percent',
    )

    percent_result = mongo_conn.find(
        task_id = id
    )


    for row in percent_result:
        pass


    try:
        row
    except UnboundLocalError, e:
        return HttpResponse(result)



    try:
        row['percent']
    except UnboundLocalError, e:
        row = {}
        row['percent'] = 0


    status = ""
    if row['status'] == "running":
        status = "progress progress-striped active"
    elif row['status'] == "success":
        status = "progress progress-success"

    if row['percent'] == 0:
        result = ""
    else:
        result = """
        <div class="%s">
            <div class="bar" style="width: %d%%;"></div>
        </div>
        """ % (status, row['percent'])


    for row in Content.objects.filter(id=id).values():
        pass


    p = Percent(id, row['project'], row['project'], str(row['env']))
    p.analyze()


    return HttpResponse(result)



