#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'xueqian Lu'

import logging

from transwrap.web import get, view
from models import User, Blog, Comment

@view('blogs.html')
@get('/')
def index():
    blogs = Blog.find_all()
    user = User.find_first('where email=?', 'admin@example.com')
    return dict(blogs=blogs, user=user)
