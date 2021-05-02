# zlktqa

#### 项目介绍
知了课堂学习的代码

#### 软件架构
软件架构说明


#### 安装教程
生成requirements.txt文件
pip freeze > requirements.txt
安装requirements.txt依赖
pip install -r requirements.txt

#### 使用说明

1、models新增模型
2、manage.py导入models新增的模型
3、根目录下执行命令python manage.py db init
4、报错提示：importError：no module named flask_script
5、则需要增加虚拟环境：source ~/Virtualenv/flask-env/bin/activate
6、迁移文件：python manage.py db migrate
报错提示：sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1045, "Access denied for user 'root'@'l
ocalhost' (using password: YES)"),
1）一般是因为你的远程数据库和你项目中的配置文件里,连接数据库的密码不一样导致的.
2）先去查看你的表： select user,host from mysql.user; 看看是不是有用户名为空的用户，有的话干掉它。
7、执行命令：python manage.py db upgrade，则数据库同步到对应的库表
报错信息：
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1862, 'Your password has expired. To lo
g in you must change it using a client that supports expired passwords.')
1）修改用户状态：update mysql.user  set password_expired = 'N' WHERE User = 'root' AND Host = 'localhost' 
备注：User和host的主键，where条件要同时加上，否则执行报错
2）重新将用户密码修改下

8、修改models，如增加字段，增加字段注释等，需要重新执行命令 python manage.py db migrate -m "Initial migration"
![img_1.png](img_1.png)
这时候输出的信息就有我们改动的字段，migrations\versions下会增加一个py的迁移脚本文件,检查表格以及字段。
![img_2.png](img_2.png)
9、再次更新数据库：更新数据库 python manage.py db upgrade,对应的users表的字段注释已更新
![img_3.png](img_3.png)


#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)