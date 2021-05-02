# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/1
@Auth ： zhangqimin
@File ：models.py
@IDE ：PyCharm

"""
from exts import db
import shortuuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # 表名
    __tablename__ = "users"
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid, comment='主键id')
    telephone = db.Column(db.String(11), nullable=False, comment='手机号码')
    username = db.Column(db.String(50), nullable=False, comment='用户名')
    password = db.Column(db.String(100), nullable=False, comment='密码')

    def __init__(self, *args, **kwargs):
        telephone = kwargs.get("telephone")
        username = kwargs.get("username")
        password = kwargs.get("password")

        self.telephone = telephone
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # datetime.now()获取的是服务器第一次运行的时间
    # datetime.now每次创建一个模型的时候，都获取当前的时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.String(100), db.ForeignKey('users.id'))
    # db.relationship()用于在两个表之间建立一对多关系。实现这种关系时，要在“多”这一侧加入一个外键，指向“一”这一侧联接的记录。
    author = db.relationship('User', backref='questions')


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    author_id = db.Column(db.String(100), db.ForeignKey('users.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    question = db.relationship('Question', backref=db.backref('answers', order_by=create_time.desc()))
    author = db.relationship('User', backref=db.backref('answers'))