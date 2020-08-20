from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer,nullable=True)
    phone = db.Column(db.String(50), nullable=False, unique=True) #unique表示必须是唯一的
    join_time = db.Column(db.DateTime, default=datetime.now )

    def __init__(self,phone,password,username):
        self.username = username
        self.password = password
        self.phone = phone

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result

    def to_json(self):
        json_user = {
            'id':self.id,
            'username':self.username,
            'phone':self.phone,
            'age':self.age

        }
        return json_user


class Swtc(db.Model):
    __tablename__ = 'swtctop_ex'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(256), nullable=False)
    swtc = db.Column(db.Numeric, nullable=False)
    cnt = db.Column(db.Numeric,nullable=True)
    hjt = db.Column(db.Numeric,nullable=True)
    jcc = db.Column(db.Numeric,nullable=True)
    vcc = db.Column(db.Numeric,nullable=True)


    def to_json(self):
        json_swtc = {
            'id':self.id,
            'address':self.address,
            'swtc':self.swtc,
            'cnt':self.cnt,
            'hjt':self.hjt,
            'jcc':self.jcc,
            'vcc':self.vcc
        }
        return json_swtc



class swtctop(db.Model):
    __tablename__ = 'swtc_address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(256), nullable=False)


    def to_json(self):
        json_swtc = {
            'id':self.id,
            'address':self.address,
        }
        return json_swtc
