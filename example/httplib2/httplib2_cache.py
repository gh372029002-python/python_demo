#!/usr/bin/python
#coding=utf-8

import httplib2
#��ȡHTTP����
h =httplib2.Http('.cache')
#����ͬ�����󣬲���ȡ����
resp, content = h.request("http://www.weirdbird.net/sitemap.xml")
print resp
# print content

print("......"*3)
httplib2.debuglevel = 1
h1 = httplib2.Http('.cache')
resp,content = h1.request('http://www.weirdbird.net/sitemap.xml')

print(resp)
print('debug',resp.fromcache)