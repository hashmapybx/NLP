## 2020年 02月 10日 星期一 15:30:30 CST 
### 会议内容

1.肺炎注册的数据整理 三个数据库(原始、基础、标注)整理完成
肺炎三个数据库数据整理花费时间：4d 截止02.08下午

肺炎体系的四级文件花费时间：1d,截止02.08晚上

2.关于结节分割的训练集是否需要整理（与晓媛确认一下）这个先是延迟到复工在讨论确定

3.等保注册项目的材料准备 今天弄好 明天给恺哥


4. 新的一批肺炎的标注数据需要补充到肺炎体系注册的数据库里面

关于肺炎数据库的脱敏日志和清洗日志后面具体的跑代码 生成log的文件

公司开发环境

 .开发环境
 
 .测试环境
 
 .演示环境
  给产品看
  演戏 彩排
 .生产环境
    真实环境
    
## 路由管理
 使用新的方案：
 蓝图 blueprint 
 使用过程先是安装
    pip install flask-blueprint
 初始化
    创建blurprint对象
        参数1：name  
        参数2：导入的name __name__
    需要使用app进行初始化
    需要注册到app上面      
 使用
    和Flask对象产不多
    直接作为装饰器用来注册路由
     
## 数据库
 sqlalchemy
 安装
    pip install flask-sqlalchemy
 初始化
    1.需要使用app进行SQLAlchemy对象的构建
        2.使用懒加载的方式init_app(app) 来进行初始化 
    sqlalchemy_database_uri 
        连接数据库的路径
        数据库+驱动://user:pass@主机:port/库
    sqlalchemy_track_modifications
        将来版本要添加的一个特征
        默认是False
             
 使用
    定制orm的操作
    定制模型 继承Model
    创建字段models.Column()
    创建库 手动 create database 库name 
    创建表
        sqlalchemy对象创建。create_all()
        删除 drop_all()
        不能差量更新
    简单的数据存储操作
        存储
            创建对象
            sqlalchemy.session.add()
            添加完了 需要commit()操作
            sqlalchemy.session.commit()
    我们发现当model发生变化的时候 我们需要更新数据库中的结构 必序要把原来的结构先是删除掉
    在去执行creatr_all()操作的 我们考虑利用flask-migarte组件
 flask-migrate:
    安装: pip install flask-migrate
    创建对象：Migrate()
    初始化对象 调用init_app(app, sqlalchemy对象) 进行初始化操作
    在manager.py 文件中执行下面的操作
    manager.add_command('db', MigrateCommand）
    使用: 在命令行执行 python manaager.py db init 产生数据迁移文件
    python manager.py db migrate
    python manager.py db upgrade 
    则是顺利完成数据库迁移 
    查看mysql数据库
     
       
 
## 请求钩子
- before_first_request
- before_request
- after_request
- teardown_request
- 面向切面基本编程
- 动态的接入请求流程

## Django的请求流程
- urls -> views
- views -> models
- models -> views
- views -> response 客户端

- 添加中间件 钩子函数
- client -> process_request[]
- process_request 逐个进行处理
- process_request -> urls
- urls -> process_view
- process_views -> views
- views -> models
- models -> views
- views -> response
- reponse -> process_response
- 逐个进行process_response
 

## 四大内置对象
- session
- request
- g 
    - 可以全局传递参数 跨函数传递
    - 间接传递数据
- config(app)
    - python代码里面获取config current_app(来自于flask对象)
        current_app.config
    - 一定的是在项目启动之后

## 会议内容
- 拉取公开测试集到Nas上面的 同步到晓媛
- 检查CFDA里面数据的时间是否正确 修改数据入库的时间
- 

## 用户邮箱激活
- 邮箱激活
    - 在异步的发送邮件
    - 在邮件中包含激活地址
        - 激活地址接受一个一次性的token
        - token 是在用户注册的时候生成的， 存在了cache中
        - key -value 
          key =token
          value 是用户的一个唯一标识
— 短信
 -同步操作              
    
      
    
             
 
   




   