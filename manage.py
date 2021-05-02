# -*- coding: utf-8 -*-
"""
@Time ： 2021/5/1
@Auth ： zhangqimin
@File ：manage.py
@IDE ：PyCharm

"""
from flask_migrate import Migrate, MigrateCommand
from zlktqa import app
from flask_script import Manager
from exts import db
import config
#新增的models模型，需要导入到manage文件



app.config.from_object(config)
db.init_app(app)
manager = Manager(app)
#使用Migrate绑定app和db，一个是flask的app对象，一个是SQLAlchemy
migrate = Migrate(app, db)
#添加迁移脚本的命令到manager钟
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()