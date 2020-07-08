import asyncio
from aiohttp import ClientSession
import requests
import json
import time
import datetime
import pymysql

def get_swtc_address():
    url = 'https://swtcscan.jccdex.cn/sum/list/10762e05?p=0&t=SWTC_&s=100'
    respone = requests.get(url)
    rs =  json.loads(respone.text)
    # print(response.text)
    if rs.get('code') == '0':
        data = rs.get('data')
        tokens = data[4]
        address = []
        for i in tokens:
            # item['address'] = i['address']
            url = 'https://swtcscan.jccdex.cn/wallet/balance/10762e05?w=' + i['address']
            # print(i['address'])
            address.append(url)
            # item['amount'] = i['amount']
            # item['updatetime'] = datetime.datetime.now().strftime("%Y-%m-%d")
    return address


# address = get_swtc_address()
# print(address[0])


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/67.0.3396.99 Safari/537.36'}

async def hay_one_url(url,semaphore):
    async with semaphore:
        print(url)
        try:
            async with ClientSession() as session:
                async with session.get(url, headers=headers) as r:
                    return await r.json()
        except Exception as e:
            print('请求异常： ' + str(e))
            return {}



def parse_one_page(rs):
    item = {}
    item['address'] = 0
    item['cnt'] = 0
    item['swtc'] = 0
    item['vcc'] = 0
    item['hjt'] = 0
    item['jcc'] = 0
    item['usdt'] = 0
    if rs.get('code') == '0':
        data = rs.get('data')
        # print(data)
        item['address'] = data.get('_id')
        if 'CNY_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or' in data:
            cntent = data.get('CNY_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or')
            item['cnt'] = cntent.get('value')
        if 'SWTC' in data:
            cntent = data.get('SWTC')
            item['swtc'] = cntent['value']
        if 'VCC_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or' in data:
            cntent = data.get('VCC_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or')
            item['vcc'] = cntent.get('value')
        if 'JJCC_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or' in data:
            cntent = data.get('JJCC_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or')
            item['jcc'] = cntent.get('value')
        if 'HJT_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or' in data:
            cntent = data.get('HJT_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or')
            item['hjt'] = cntent.get('value')
        if 'SUSDT_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or' in data:
            cntent = data.get('SUSDT_jGa9J9TkqtBcUoHe2zqhVFFbgUVED6o9or')
            item['usdt'] = cntent.get('value')
        item['updatetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(item)
    return item



async def main():
    semaphore = asyncio.Semaphore(200)
    db = swtcitem()
    address = get_swtc_address()
    # adds = address[:1]
    # tasks = []
    tasks = [hay_one_url(url,semaphore) for url in address]
    # for url in address:
    #     tasks.append(asyncio.create_task(hay_one_url(url,semaphore)))
    results = await asyncio.gather(*tasks,return_exceptions=True)
    for res in results:
        item = parse_one_page(res)
        db.process_item(item)
    db.close_db()




class swtcitem(object):
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost','root','bookan','anders')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
    def process_item(self,item):
        # print(item)
        insert_sql = """
        insert into swtctop_ex(address,swtc,cnt,jcc,hjt,vcc,usdt,updatetime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """
        try:
            # 执行插入数据到数据库操作
            self.cursor.execute(insert_sql,(item['address'],item['swtc'],item['cnt'],item['jcc'],item['hjt'],item['vcc'],item['usdt'],item['updatetime']))
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
        except Exception as e:
            print(e)
    def close_db(self):
        self.cursor.close()
        self.conn.close()



if __name__ == '__main__':
    start = time.time()

    asyncio.run(main())
    # python3.7之前的写法
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()

    print(time.time()-start)