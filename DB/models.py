from sqlalchemy import Column, Integer, String,ForeignKey,Float,TIMESTAMP,text
from datetime import datetime
from DB.database import Base

class tb_user(Base):
    __tablename__ = 'user'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True,nullable=False)
    password = Column(String(120), unique=True,nullable=False)

    # def __init__(self, username=None, password=None):
    #     self.username = username
    #     self.password = password

    # def __repr__(self):
    #     return '<User %r>' % (self.username)



class tb_post(Base):
    __tablename__ = 'post'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    author_id = Column(ForeignKey(u'user.id'))
    author_id = Column(String(50), unique=True)
    created = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    title = Column(String(50),unique=True)
    body = Column(String(500),nullable=False)




class Kegg_compound(Base):
    __tablename__ = 'kegg_compound'
    __table_args__ = {"useexisting": True}
    molecular_formula= Column(String(40), nullable=False)
    dbe= Column(Float(4), nullable=False)
    formula_weight= Column(Float(20), nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    description= Column(String(1000), nullable=False)


class Proxy(Base):
    __tablename__ = 'proxys'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(VARCHAR(16), nullable=False)
    port = Column(Integer, nullable=False)
    types = Column(Integer, nullable=False)
    protocol = Column(Integer, nullable=False, default=0)
    country = Column(VARCHAR(100), nullable=False)
    area = Column(VARCHAR(100), nullable=False)
    updatetime = Column(DateTime(), default=datetime.utcnow)
    speed = Column(Numeric(5, 2), nullable=False)
    score = Column(Integer, nullable=False, default=10)
