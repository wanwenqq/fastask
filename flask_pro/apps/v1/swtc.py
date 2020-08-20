from flask import Blueprint,views,request
import json
from apps.respone import make_respone
from apps.v1.models import Swtc
from apps.v1.models import swtctop
from exts import db


bp = Blueprint('swtc',__name__,url_prefix='/v1')

class BaseView(views.MethodView):
    def __init__(self):
        super.__init__()


class SwtclistView(BaseView):
    def __init__(self):
        self.respone = {
            'datas':None,
        }
    
    def post(self):
        datas = db.session.query(Swtc).group_by('address').limit(10).all()
        self.respone['datas'] = [item.to_json() for item in datas]
        return make_respone(self.respone, 200, '获取address列表成功')

class SwtctopView(BaseView):
    def __init__(self):
        self.respone = {
            'datas':None,
        }
    
    def post(self):
        datas = db.session.query(swtctop).limit(100).all()
        self.respone['datas'] = [item.to_json() for item in datas]
        return make_respone(self.respone, 200, '获取top address列表成功')


bp.add_url_rule(rule='/swtclist',view_func=SwtclistView.as_view('swtclist'))
bp.add_url_rule(rule='/swtctop',view_func=SwtctopView.as_view('swtctop'))