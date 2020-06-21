from flask import Flask
import config
from  flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(64),nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref='artiles')

# 1.创建数据库
# 删除当前绑定模型
# db.drop_all()
# 创建绑定
# db.create_all()

# 2.新增数据
# user = User(username='anders')
# article = Article(title='show me title')
# article.author = user

# db.session.add(article)
# db.session.commit()

# 3.修改数据
user = db.session.query(User).filter(User.username=='anders').first()
user.username = 'simon'
db.session.commit()