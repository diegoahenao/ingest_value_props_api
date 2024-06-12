from sqlalchemy import Column, Integer, String, Date, Float
from app.database.database import Base

class Taps(Base):
    __tablename__ = "taps"
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(Date)
    position = Column(Integer)
    value_prop = Column(String)
    user_id = Column(Integer)


class Prints(Base):
    __tablename__ = "prints"
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(Date)
    position = Column(Integer)
    value_prop = Column(String)
    user_id = Column(Integer)


class Pays(Base):
    __tablename__ = "pays"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pay_date = Column(Date)
    total = Column(Float)
    user_id = Column(Integer)
    value_prop = Column(String)