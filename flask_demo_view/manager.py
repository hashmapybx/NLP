import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

# 获取环境变量 代码在不同的环境下面不需要做任何的改变
env = os.environ.get("FLASK_ENV", 'develop')
app = create_app(env)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run() # 里面还是调用了app.run() 操作

