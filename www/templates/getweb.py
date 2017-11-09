#!/usr/bin/python 
#_*_ coding:utf-8 _*_

#获取网页数据
import httplib2
import urllib2

class PagerClass:
    #获取指定url的网页内容
    def get_page(self, url, headers):
        http = httplib2.Http()
        response,content = http.request(url, 'GET', headers=headers)
        return content.decode('unicode-escape').encode('utf-8')
def main():

