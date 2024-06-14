from sqlalchemy import Column, Integer, String, Date, Float, Sequence
from app.database.database import Base

id_seq = Sequence('id_seq')

class Taps(Base):
    __tablename__ = "taps"
    id = Column(Integer, id_seq, primary_key=True, server_default=id_seq.next_value())
    day = Column(Date)
    position = Column(Integer)
    value_prop = Column(String)
    user_id = Column(Integer)


class Prints(Base):
    __tablename__ = "prints"
    id = Column(Integer, id_seq, primary_key=True, server_default=id_seq.next_value())
    day = Column(Date)
    position = Column(Integer)
    value_prop = Column(String)
    user_id = Column(Integer)


class Pays(Base):
    __tablename__ = "pays"
    id = Column(Integer, id_seq, primary_key=True, server_default=id_seq.next_value())
    pay_date = Column(Date)
    total = Column(Float)
    user_id = Column(Integer)
    value_prop = Column(String)