#!/usr/bin/env python
#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2

class Webservice:
    def wget(self, url):
        if not url.startswith('http://'):
            raise Exception('url error')
        else:
            data = ''
            req = urllib2.Request(url)
            try:
                fd = urllib2.urlopen(req)
            except urllib2.HTTPError, e:
                raise ValueError('HTTP ERROR: %s' % e)
            except urllib2.URLError, e:
                raise ValueError('URL ERROR: %s' % e)
            while 1:
                data_contents = fd.read(1024)
                if not len(data_contents):
                    break
                else:
                    data += data_contents
        return data

    def wget_head(self, url):
        if not url.startswith('http://'):
            raise Exception('url error')
        else:
            req = urllib2.Request(url)
            try:
                fd = urllib2.urlopen(req)
            except urllib2.HTTPError, e:
                raise ValueError('HTTP ERROR: %s' % e)
            except urllib2.URLError, e:
                raise ValueError('URL ERROR: %s' % e)
            info = fd.info()
            return info
        
                

