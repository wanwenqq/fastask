# uwsgi+nginx+flask+ubuntu
---
1. 先确定ubuntu环境，安装python及pip相关
2. flask自己安装或导入Flask工程通过requirements
3. 安装 uwsgi: sudo install uwsgi
4. 在flask工程目录下建config目录，在config下配置uwsgi.ini
5. 尝试uwsgi --ini config/uwsgi.ini启动，并在web端访问试试
6. 安装 nginx: sudo install nginx 
    1. 所有的配置文件都在/etc/nginx下，并且每个虚拟主机已经安排在了/etc/nginx/sites-available下
    2. 程序文件：/usr/sbin/nginx
    3. 日志：/var/log/nginx
    4. 程序脚本:/etc/init.d/ ,nginx命令可以在这执行，需以root的权限执行
    5. 如nginx环境破坏，需要删除，先/etc/init.d/nginx stop
        - 删除nginx，–purge包括配置文件:sudo apt --purge remove nginx
        - 自动移除全部不使用的软件包:sudo apt autoremove
        - 列出与nginx相关的软件 并删除显示的软件:
           - dpkg --get-selections|grep nginx
           - sudo apt-get --purge remove nginx
           - sudo apt-get --purge remove nginx-common
           - sudo apt-get --purge remove nginx-core
        - 查看nginx:which nginx
7. 查看nginx -t 配置是否有问题 ，执行：/etc/init.d/nginx start，通过web访问看是否有nginx提示
8. 

