#encoding=utf-8
__author__ = 'jophyyao'


import os, sys

os.putenv('JAVA_HOME', '/usr/local/jdk')
os.putenv('PATH', '/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin:/root/bin:/jre/bin')
os.putenv('CLASSPATH', '/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin:/root/bin:/jre/bin:/lib/tools.jar:/lib/dt.jar')
os.putenv('JETTY_HOME', '/usr/local/ctier/pkgs/jetty-6.1.21')
os.putenv('CTL_BASE', '/usr/local/ctier/ctl/')


if not os.path.abspath(os.path.dirname(__file__)) in sys.path[:1]:
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'autorelease.settings'
    from django.core.handlers.wsgi import WSGIHandler
    application = WSGIHandler()