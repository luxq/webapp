#!/usr/bin/python 
#_*_ coding:utf-8 _*_

#from urllib import *
import urllib2
from bs4 import BeautifulSoup
import ConfigParser
import HTMLParser
import lxml
from lxml import etree
#import MySQLdb
import mysql.connector


#解析url文件
class ConfigUrl:
    InFilename = ''
    UrlMap = {}
    UrlEncodeMap = {}

    def __init__(self):
        pass

    def ParseInit(self, file):
        '''
        获取url,及字符集
        '''
        conf = ConfigParser.ConfigParser()
        #用config对象读取配置文件
        conf.read(file)
        #获取所有url及字符集
        key = 0
        for url,value in conf.items("UrlName set"):
            value = value + ':'
            url=value + url
           # print url
            self.UrlMap[key]=url
           # print self.UrlMap[key]
            key = key + 1

        print "first key:",key

        '''
        key = 0
        for encode,value in conf.items("UrlEncode set"):
            if value != "false":
                self.UrlEncodeMap[key] = encode
                print self.UrlEncodeMap[key]
                key = key +1
        print "seconde key:",key
        '''


#解析一个指定的url
class ParseUrl:
    #获取网页内容
    def get_content(self, url):
        html=urllib2.urlopen(url)
        html_content=html.read()
      #  if SrcEncode != DstEncode:
        #html_content.encode('utf8')

       # print html_content
       # bsObj = BeautifulSoup(html_content,'html.parser')
       # return bsObj
        html.close()
        return html_content


    #转换网页字符集
    def exchange_encode(self, HtmlContent, SrcEncode, DstEncode):
        return HtmlContent.decode(SrcEncode).encode(DstEncode)






def main():
    conf=ConfigUrl()
    node_list = []
    #创建连接
    config={ 
            'host':'172.26.3.19',
            'user':'root',
            'password':'root',
            'port':3306,
            'database':'HAPPY_MM',
            'charset':'utf8'
            }
    conn=mysql.connector.connect(**config)
    #创建游标
    cur=conn.cursor()
    conf.ParseInit('./UrlConfig.ini')
    for key in conf.UrlMap:
        TestUrl = ParseUrl()
        #url = 'http:'+conf.UrlMap[key]
        html = TestUrl.get_content(conf.UrlMap[key])
        print conf.UrlMap[key]
        #print html

        #字符集转化
        #if (conf.UrlMap[key]!='utf-8'):
         #   html=TestUrl.exchange_encode(html,conf.UrlMap[key],'utf-8')


        #获取html文件中所有的div，class属性为post_item_body节点
        #PostItemBody = bsObj.find_all("div",class_="post_item_body")
        #print PostItemBody
        #获取节点内容
        tree = etree.HTML(html)
        #result = etree.tostring(html)
        nodes = tree.xpath('//div[@class="post_item_body"]')
        nodes_count = len(nodes)
        print "title:",nodes_count
        for i in range(nodes_count):
            node_str = ""
            data={}
            #获取标题
            node = nodes[i].xpath("h3/a")
            for n in node:
                #print "title: ",n.text
                node_str = n.text
                node_utf = node_str.replace("\n","")
                data['TITLE']=node_utf

            #获取内容
            node = nodes[i].xpath('p[@class="post_item_summary"]')
            for n in node:
                #print "内容： ",n.text
                content = n.text
                content = content.replace("\n","")
                data['CONTENT']=content
                #node_str = node_str + content
                #print node_str


            #获取发布时间
            node = nodes[i].xpath('div[@class="post_item_foot"]')
            for n in node:
              # print "发布时间：", (n.xpath('string(.)'))
               node_str = n.xpath('string(.)')
               my_node =""
               my_node=node_str.replace("\u","")
               strlist=my_node.split('\r\n')
               i=0
               value_str = []
               for value in strlist:
                   i=i+1
                   if i==2:
                       data['AUTHOR']=value
                      # print "author:",value
                   elif i==3:
                       data['PUBLIC_TIME']=value
                      # print "时间：",value
                   elif i==5:
                       #获取阅读数
                       copy=False 
                       finished=False
                       mstr=""
                       strmp={}
                       i=0
                       for s in value:
                           if s=='(':
                               copy=True 
                               continue
                           elif s==')':
                               finished=True
                           if copy and s!='(' and s!=')':
                               mstr=mstr+s
                           if finished:
                               copy=False 
                               strmp[i]=mstr
                               i=i+1
                               mstr=""
                               finished=False 
                               
                       #获取浏览数
                       data['COMMENT_NUMBER']=int(strmp[0])
                       data['VIEW_NUMBER']=int(strmp[1])
            insert_str="insert into BLOG_DATA(TITLE,CONTENT,AUTHOR,PUBLIC_TIME,COMMENT_NUMBER,VIEW_NUMBER) values (%(TITLE)s,%(CONTENT)s,%(AUTHOR)s,%(PUBLIC_TIME)s,%(COMMENT_NUMBER)s,%(VIEW_NUMBER)s)"
            ret_cur=cur.execute(insert_str,data)
            #提交事物，否则数据无法真正插入数据库
            conn.commit()

    if cur:
        cur.close()
    if conn:
        conn.close()






                  
    
if __name__ == "__main__":
    main()

