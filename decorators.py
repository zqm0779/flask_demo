# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/1
@Auth ： zhangqimin
@File ：decorators.py
@IDE ：PyCharm

"""
from functools import wraps
from flask import session, redirect, url_for, g

#装饰器，判断用户是否已登录，否则跳转到登录页面
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, 'user'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper