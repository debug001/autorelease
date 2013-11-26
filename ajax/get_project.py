#encoding=utf-8
__author__ = 'jophyyao'

from django.http import HttpResponse
from task.models import Project

def index(request):
    response=HttpResponse()
    #response['Content-Type']="text/javascript"
    project=request.POST.get("project",'').lower()

    ret=""
    result=""

    dt = {}

    if project:
        ret = Project.objects.filter(type=project)
        ret = ret.values()
        for row in ret:
            if dt.has_key(row['name']):
                continue
            result += row['name']+"|"
            dt[row['name']] = 0
    else:
        result="error"

    response.write(result)
    return response
