import config


from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(config.DB_URI)
# conn = engine.connect()
# result = conn.execute('select version()')
# print(result.fetchone())

Base = declarative_base(engine)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)

Base.metadata.create_all()