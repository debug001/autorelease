#encoding=utf-8
__author__ = 'jophyyao'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import django_cas
from models import Validation
import re

#=====================================
# url return code validation
def url(request, project, env):
    from lib.node import Node
    from lib.common import Common

    result = ""

    n = Node(project, env)
    ip = []
    for row in n.get():
        if row['hostname'].startswith("Controltier"):
            continue
        ip.append(row['hostname'])

    for vrow in Validation.objects.filter(project=project).values():
        for server in ip:
            if vrow['url'].startswith("ip"):
                url = re.sub("ip" , server, vrow['url'])
                return_code = Common().get_return_code(url, vrow['port'])
                result += """
                <tr>
                    <th>{url}</th>
                    <th>{return_code}</th>
                </tr>
                """.format(
                    url = url,
                    return_code = return_code,
                )

    return HttpResponse(result)
