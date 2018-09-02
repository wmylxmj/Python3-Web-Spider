# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 19:17:38 2018

@author: wmy
"""

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
# <class 'http.client.HTTPResponse'>
print(type(response))
# 200
print(response.status)
print(response.getheaders())
# 服务器是使用nginx搭建的
print(response.getheader('Server'))

# post请求
import urllib.parse

data = bytes(urllib.parse.urlencode({'word': 'hellow'}), encoding = 'utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# timeout
response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

# 超时跳过抓取
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
