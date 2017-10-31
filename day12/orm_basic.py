# author: poke

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

engine = create_engine("mysql+pymysql://poke:poke@192.168.137.132:3306/pokedb", encoding='utf-8', echo=False)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(12))
    password = Column(String(64), server_default='123456')

    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (self.name, self.password)


Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()

# user_obj = User(name='wangkai', )
# user_obj1 = User(name='xuecheng', password='poke')
# user_obj2 = User(name='bobo', password='poke')
# user_obj3 = User(name='qilin', )
# user_obj4 = User(name='poke', password='poke')
# user_obj5 = User(name='1poke1', password='poke1')
# session.add_all({user_obj, user_obj1, user_obj2, user_obj3, user_obj4, user_obj5})
my_user = session.query(User).filter(User.name.like("%poke%")).filter(User.password == 'poke').all()
print(my_user)
# session.commit()
print(session.query(User.name, User.password).filter().count())

print(session.query(func.count(User.name), User.name).group_by(User.name).having(func.count(User.name) == 1).all())
