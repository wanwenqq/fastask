# 用户信息管理
from flask import Blueprint,views,request
import json
from utils import common
from apps.respone import make_respone
from apps.v1.models import User
import config
from exts import db

bp = Blueprint('user',__name__,url_prefix='/v1')

class BaseView(views.MethodView):
    def __init__(self):
        super.__init__()


class LogonView(BaseView):
    def __init__(self):
        self.respone = {
            'id':None,
            'phone':None,
            'token':None
        }
    
    def post(self):
        data = request.get_data()
        json_re = json.loads(data)
        phone = json_re['phone']
        password = json_re['password']
        if common.isPhone(phone) or password is None:
            # return make_respone(data={},message='用户名或密码错误',status=601)
            return make_respone(None,400,'用户名或密码错误')
        else:            
            user  = User.query.filter_by(phone=phone).first()
            if user and user.check_password(password):
                # 根据userid生成token,并返回给前端
                token = common.make_token(str(config.TOKEN_KEY))
                self.respone['id'] = user.id
                self.respone['phone'] = user.phone
                self.respone['token'] = token
                # 在redis中记录token的值
                # RedisCache().set_data(user.id, token)
                # 返回登录成功包
                return make_respone(self.respone, 200, '登录成功')
            else:
                return make_respone(None, 403, '登录失败') 



class RegisterView(BaseView):
    def __init__(self):
        self.respone = {
            'id':None,
            'phone':None,
            'token':None
        }
    def post(self):
        data = request.get_data()
        json_re = json.loads(data)
        phone = json_re['phone']
        password = json_re['password']
        username = json_re['username']
        if common.isPhone(phone) or password is None:
            return make_respone(None,400,'用户名或密码设置错误')
        else:
            user =  User(username=username,phone=phone,password=password)
            try:
                db.session.add(user)
                db.session.commit()
                return make_respone(None,200,'注册成功')
            except Exception as e:
                print(e)
                return make_respone(None,600,'注册失败')

class UserlistView(BaseView):
    def __init__(self):
        self.respone = {
            'datas':None,
        }
    
    def post(self):
        datas = db.session.query(User).all()
        self.respone['datas'] = [item.to_json() for item in datas]
        return make_respone(self.respone, 200, '获取用户列表成功')



bp.add_url_rule(rule='/login',view_func=LogonView.as_view('login'))
bp.add_url_rule(rule='/register',view_func=RegisterView.as_view('register'))
bp.add_url_rule(rule='/userlist',view_func=UserlistView.as_view('userlist'))


