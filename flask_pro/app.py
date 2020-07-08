from flask import Flask,make_response,request
import config

from apps.v1 import data_bp,user_bp
from apps.ips import ips
from apps.auths import auths
from utils.slogging import logger
from apps.respone import my_abort,make_respone

from exts import db 



logger.info('初始化flask')
#创建一个Flask对象，传递__name__参数
#__name__参数作用
#1. 可以规定模板和静态文件的查找路径
#2. 以后一些插件报错了，可以通过这个参数找到具体的错误位置
# 1.应用初始化
app = Flask(__name__)
# 2.读取配置文件
logger.info('读取配置文件')
app.config.from_object(config)
# 3.初始化数据库
logger.info('初始化数据库')
db.init_app(app)
# 4.注册蓝图
logger.info('注册蓝图')
app.register_blueprint(data_bp)
app.register_blueprint(user_bp)
# 5.自定义异常处理
logger.info('注册自定义异常处理')
app.abort = my_abort

# 6.请求前处理逻辑
logger.info('注册请求前处理逻辑')
@app.before_request
def print_request_info():
    # print("请求地址：" + str(request.path))
    # print("请求方法：" + str(request.method))
    # print("---请求headers--start--")
    # print(str(request.headers).rstrip())
    # print("---请求headers--end----")
    # print("GET参数：" + str(request.args))
    # print("POST参数：" + str(request.form))
    print(request.remote_addr)

    #可在此处检查jwt等auth_key是否合法，
    #abort(401)
    #然后根据endpoint，检查此api是否有权限，需要自行处理
    #print(["endpoint",connexion.request.url_rule.endpoint])
    #abort(401)
    #也可做ip检查，以阻挡受限制的ip等
    if filter_request(request):
        return make_respone(None,403,'你被禁了')
    # if is_auth_request(request):
    #     token = request.headers.get('Token',None)
    #     if not token:
    #         # 如果 header中没有Token需要重新登录
    #         return make_respone(None,403,'没有权限，请重新登录1')
    #     else:
    #         if not certify_token(config.TOKEN_KEY,token):
    #             # 如果 header中有Token但是校验没有通过
    #             return make_respone(None,403,'没有权限，请重新登录2')

# 非鉴权请求
def is_auth_request(request):
    if request.path in auths:
        return False
    return True
# 过滤IP地址
def filter_request(request):
    if request.remote_addr in ips:
        return True
    return False 



# 7.请求后处理逻辑
logger.info('注册请求后处理逻辑')
# 跨域支持
def after_request(resp):
    # //允许所有来源访问
    resp.headers['Access-Control-Allow-Origin'] = '*'
    # //用于判断request来自ajax还是传统请求
    resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    # //允许访问的方式
    resp.headers['Access-Control-Allow-Methods'] = 'PUT,POST,GET,DELETE,OPTIONS'
    # //内容类型：如果是post请求必须指定这个属性
    resp.headers['Content-Type'] = 'application/json;charset=utf-8'
    return resp


app.after_request(after_request)


logger.info('完成flask初始化，开始工作')
#@app.route是一个装饰器
#@app.route('/')就是将url中的/映射到hello_world这个视图函数上面
#当你访问网站/目录的时候，会执行hello_world函数，然后这个函数的返回值给浏览器
@app.route('/')
def hello_world():
    return 'hello world'




#如果这个文件是作为一个主文件运行，那么执行app.run()方法，即启动网站
#app.run()是flask中的一个测试应用服务器
if __name__ == '__main__':
    app.run()