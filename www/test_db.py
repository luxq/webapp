#!/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'xueqian Lu'

import transwrap.db as db
from models import User,Blog,Comment

db.create_engine(user='test', password='Avl1108', database='test')
u = User(name='Test', email='test@example.com', password = '12345678', image='about:blank')

u.insert()
print 'new user id:', u.id

u1 = User.find_first('where email=?', 'test@example.com')
print 'find user\'s name:', u1.name
u1.delete()

u2 = User.find_first('where email=?', 'test@example')
print 'find user:', u2
