# linux环境搭建 ubuntu,centos类似
1. 修改系统默认源为阿里云
   - 备份：cp /etc/apt/sources.list /etc/apt/sources.list.bak
   - 在此添加阿里源：vi /etc/apt/sources.list
2. 源码安装python3,pip
3. 安装mysql并配置mysql
4. 安装redis
5. pip install -r requirements.txt 或 pip3 install -r requirements.txt
6. 配置数据库，修改config.product.py为 confing.py,并修改相关参数
7. 启动服务测试:当前目录下python3 app.py 或 python app.py 
8. 正式使用：安装配置nginx,supervisor，参考[config/README.MD](config/README.MD)

---
centos 7 不同ubuntu的地方
---
1. python3.X安装不同，注意与2.X兼容问题
2. nginx,uwsgi配置注意


# python flask 
---
1. **基础类库**
2. **使用SQLAchemy和flaskk_SQLAchemy**
    
    1. pip install pymysql
    2. pip install flask-sqlalchemy
    3. pip install flask-script
    4. pip install flask-migrate
    5. 在config.py文件中配置mysql账号相关信息
    6. 在exts.py文件中实例sqlalchemy为db,避免多文件重复循环引用
    7. 在models.py中定义各种模型类
    8. 在主文件(入口文件)中引用exts中的db,并进行db.init_app(app)初始化工作，记得在Flask app初始化后
    9. 定义manager.py，通过flask-script和flask-migrate来管理数据的相关工作(CURD)
        - python manage.py db init
        - python manage.py db migrate
        - python manage.py db upgrade
        - python manage.py 函数名 参数1 参数2 ...
3. 配置uwsgi和nginx，见[config/README.MD](config/README.MD)
4. (**linux**)安装supervisor,管理uwsgi:pip install supervisor,配置见[config](config/supervisor.conf)
    - 1.supervisord -c supervisor.conf 启动uwsgi服务
    - 2.supervisorctl -c supervisor.conf 到管理控制台
        status # 查看状态
        start program_name #启动程序
        restart program_name #重新启动程序
        stop program_name # 关闭程序
        reload # 重新加载配置文件
        quit # 退出控制台
5. mysql 账号登录问题和group by在5.7版本以上的问题
6. pip freeze > requirements.txt 换成 pipreqs --force ./ 只取当前项目lib
7.
