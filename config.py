# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/1
@Auth ： zhangqimin
@File ：config.py
@IDE ：PyCharm

"""
import os
#数据库的配置
HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'zlktqa'
USERNAME = 'root'
PASSWORD = 'Pass@word1'
#指定配置用来省略提交操作
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
print(SQLALCHEMY_DATABASE_URI)


# 这一行不加会有警告
SQLALCHEMY_TRACK_MODIFICATIONS = True


DEBUG = True
#随即产生n个字节的字符串，可以作为随机加密key使用~
SECRET_KEY = os.urandom(24)