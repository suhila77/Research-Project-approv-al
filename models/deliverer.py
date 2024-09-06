#!/usr/bin/python3

from sqlalchemy import Column, String
from models.base import Base, Session

class Deliverer(Base):
    __tablename__ = 'deliverers'
    email = Column(String, primary_key=True)
    password = Column(String)
    name = Column(String)

def add_deliverer(email, password, name):
    session = Session()
    if session.query(Deliverer).filter_by(email=email).first():
        print("Deliverer already exists.")
        session.close()
        return
    new_deliverer = Deliverer(email=email, password=password, name=name)
    session.add(new_deliverer)
    session.commit()
    session.close()

def update_deliverer(email, password, name):
    session = Session()
    deliverer = session.query(Deliverer).filter_by(email=email).first()
    if deliverer:
        deliverer.password = password
        deliverer.name = name
        session.commit()
    session.close()
