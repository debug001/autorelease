#encoding=utf-8
__author__ = 'jophyyao'


import os, sys
if not os.path.abspath(os.path.dirname(__file__)) in sys.path[:1]:
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    from django.core.handlers.wsgi import WSGIHandler
    application = WSGIHandler()