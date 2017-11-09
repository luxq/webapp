#!/usr/bin/python 
#_*_ coding:utf-8 _*_
import mysql.connector
config={'host':'127.0.0.1',
        'user':'root',
        'password':'root',
        'port':3306,
        'database':'HAPPY_MM',
        'charset':'utf8'}
try:
    cnn=mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
