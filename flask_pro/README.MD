# linux环境搭建
1. 修改系统默认源为阿里云
   - 备份：cp /etc/apt/sources.list /etc/apt/sources.list.bak
   - 在此添加阿里源：vi /etc/apt/sources.list
2. 源码安装python3,pip
3. 安装mysql并配置mysql
4. 安装redis


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
    8. 的主文件(入口文件)中引用exts中的db,并进行db.init_app(app)初始化工作，记得在Flask app初始化后
    9. 定义manager.py，通过flask-script和flask-migrate来管理数据的相关工作(CURD)
        - python manage.py db init
        - python manage.py db migrate
        - python manage.py db upgrade
        - python manage.py 函数名 参数1 参数2 ...
3. 配置uwsgi和nginx，见[config/README.MD](config/README.MD)
4. (**linux**)安装supervisor,管理uwsgi:pip install supervisor,配置见[config](config/supervisor.conf)
5. 
6.
7.
