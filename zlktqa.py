# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/1
@Auth ： zhangqimin
@File ：zlktqa.py
@IDE ：PyCharm

"""
from flask import render_template, request, session, redirect, url_for, g
from exts import db

from flask import Flask
import config
from decorators import login_required
from sqlalchemy import or_

from models import Question, User, Answer

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


# 首页
@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by(Question.create_time.desc()).all()
    }
    return render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 获取html页面输入的手机号码即属性：name="telephone"
        telephone = request.form.get("telephone")
        password = request.form.get("password")
        # 根据页面输入的手机号码，查询数据库的手机号码是否存在于表
        user = User.query.filter(User.telephone == telephone).first()
        # 判断手机号码已注册，且密码是正确的
        if user and user.check_password(password):
            # 将用户id添加到session
            session['user_id'] = user.id
            # 如果想在31天内都不需要登录
            session.permanent = True
            # g：global
            # 1. g对象是专门用来保存用户的数据的。
            # 2. g对象在一次请求中的所有的代码的地方，都是可以使用的。
            g.user = user
            # 登录成功跳转到首页
            # url_for就是高级版的重定向redirect
            return redirect(url_for("index"))
        else:
            return "用户名不存在或密码错误"


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 页面表单的name属性
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u"用户名已存在"
        else:
            if password1 != password2:
                return u"密码不一致"
            else:
                # 将界面输入的数据，插入user表
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                # 注册成功，则跳转到登录页面
                return redirect(url_for("login"))


# 视图函数之后
# 1.上下文处理器应该返回一个字典，字典中的key会被模板中当成变量来渲染
# 2.上下文处理器返回的字典，在所有页面中都是可以使用的
# 3.被这个装饰器修饰的钩子函数，必须要返回一个字典，即使为空也要返回。@app.context_processor
def my_context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    return {}


@app.route('/logout/', methods=['GET'])
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for("login"))


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)

        question.author = g.user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


# question_id参数传值
@app.route('/detail/<question_id>')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)


@app.route("/add_answer/", methods=["POST"])
@login_required
def add_answer():
    content = request.form.get("answer_content")
    question_id = request.form.get("question_id")
    answer = Answer(content=content)

    answer.author = g.user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


@app.route("/search/")
@login_required
def search():
    q = request.args.get("q")
    questions = Question.query.filter(or_(Question.title.contains(q), Question.content.contains(q))).order_by(
        Question.create_time.desc())
    if questions:
        return render_template("index.html", questions=questions)
    else:
        return u"查询不到数据！"


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user


if __name__ == '__main__':
    app.run()