from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

import config

# 1.根据数据库配置创建引擎
engine  =  create_engine(config.DB_URI)
# 2.根据engine创建一个ORM基类
Base = declarative_base(engine)
# 3.定义模型
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(64),nullable=False)
    age = Column(Integer,nullable=False)

# 4.映射模型
Base.metadata.create_all()