# -*- coding: utf-8 -*-

import asyncio
from aiohttp import ClientSession
import requests
import json
import time
import datetime
import pymysql
'''
# https://github.com/JCCDex/jcc_server_doc/blob/master/README.md
# 从上面的接口中获取服务器列表 
# 1 获取服务器列表
# HTTP请求
# GET https://jccdex.cn/static/config/jc_config.json
# 请求参数: 无
# 返回参数: 所有服务器配置信息，配置说明如下:
# exHosts：交易服务器列表，默认端口为80
# infoHosts：信息服务器列表，默认端口为80
# 说明
# 以下所有API请求对应的host都是基于exHosts或者infoHosts的
# 接口路由中以/exchange开头的请调用exHosts列表中服务器
# 接口路由中以/info开头的请调用infoHosts列表中服务器
# 为了减轻单个服务器负载，请用轮询机制分别访问列表中每台服务器
'''

def get_jcc_website():
    url = 'https://jccdex.cn/static/config/jc_config.json'
    respone = requests.get(url)
    # print(respone.text)
    rs =  json.loads(respone.text)
    exHosts = rs['exHosts']
    infoHosts = rs['infoHosts']
    # print(len(infoHosts))
    return exHosts,infoHosts


async def main():
    semaphore = asyncio.Semaphore(200)
    db = jccitem()
    exHosts,infoHosts = get_jcc_website()

    for ex in exHosts:
        db.process_item(ex,'ex')
    for info in infoHosts:
        db.process_item(info,'info')
    db.close_db()

class jccitem(object):
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost','root','12345678','flaskori')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
    def process_item(self,item,type):
        print(item,type)
        insert_sql = """
        insert into jcc_site(site,type) VALUES(%s,%s)
        """
        try:
            # 执行插入数据到数据库操作
            self.cursor.execute(insert_sql,(item,type))
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
        except Exception as e:
            print(e)
    def close_db(self):
        self.cursor.close()
        self.conn.close()



if __name__ == '__main__':
    asyncio.run(main())
    # get_jcc_website()


