# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:07:09 2018

@author: wmy
"""

import urllib.request
import urllib.error
import urllib.parse
import requests
import requests.packages
import logging
import re
import chardet
import lxml.etree

class BilibiliSpider():
    
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                        'Cookie': 'buvid3=552DFA0C-00DB-4A62-8B4D-07ED013BEA6F101570infoc; LIVE_BUVID=AUTO3715298368330790; sid=kplk3t9k; _uuid=FF2F7BFB-F27B-CCE7-8AE1-0914DC7741EA52188infoc; finger=7360d3c2; DedeUserID=252185756; DedeUserID__ckMd5=16ee9c88dd47b66f; SESSDATA=314d5403%2C1541575079%2C71133822; bili_jct=37bf3c0ad83f143f87d82095046b3a33; fts=1538983089; _dfcaptcha=37736c2d46cd05ca6e40edd10c0ef994'}
        self.data = {'name': 'wmylxmj',
                     'tool': 'Python-3.6'}
        self.url_homepage = 'https://www.bilibili.com'
        pass
    
    def get_homepage_html(self, verify=True, timeout=None, print_flag=False):
        url = self.url_homepage
        headers = self.headers
        data = self.data
        try:
            response = requests.get(url, headers=headers, data=data, verify=verify, timeout=timeout)
        except:
            print('Request Failed')
            return None
        else:       
            if response.status_code == 200:
                print('Request Successfully')
                if print_flag:
                    print(response.text)
                return response.text
            print('Request Failed', 'status code:' + response.status_code)
            return None
        return None
    
    def get_html_homepage_infomation(self, print_flag=False):
        pattern = re.compile('<p.*?title">(.*?)</p>')
        html = self.get_homepage_html()
        items = re.findall(pattern, html)
        for item in items:
            if print_flag and len(item) >= 1:     
                print('***********************************************************')
                print(item)
                pass
            pass
        return items
    
    def download_bilibili_icon(self):
        try:    
            req = requests.get('https://www.bilibili.com/favicon.ico')
            with open('bilibili_favicon.ico', 'wb') as file:
                file.write(req.content)
        except:
            print('Download Failed.')
            return
        print('Download Finished!')
        pass
    
    def download_homepage(self):
        url = 'https://www.bilibili.com'
        headers = self.headers
        data = self.data
        try:
            response = requests.get(url, headers=headers, data=data)
        except:
            print('Download Failed.')
            return None
        else:       
            if response.status_code == 200:
                with open('bilibili_homepage.htm', 'wb') as file:
                    file.write(response.content)
                print('Download Finished!')
                return None
            print('Download Failed.')
            return None
        return None
    
    pass

bs = BilibiliSpider()
bs.get_homepage_html(print_flag=True)
bs.get_html_homepage_infomation(print_flag=True)
bs.download_bilibili_icon()
bs.download_homepage()
