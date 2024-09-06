#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from models.base import Base, Session

class Customer(Base):
    __tablename__ = 'customers'
    email = Column(String, primary_key=True)
    password = Column(String)
    name = Column(String)
    phone = Column(String)
    wallet_balance = Column(Integer, default=0)

def add_customer(email, password, phone, name):
    session = Session()
    if session.query(Customer).filter_by(email=email).first():
        print("Customer already exists.")
        return
    new_customer = Customer(email=email, password=password, phone=phone, name=name)
    session.add(new_customer)
    session.commit()
    session.close()

def update_customer(email, password, name):
    session = Session()
    customer = session.query(Customer).filter_by(email=email).first()
    if customer:
        customer.password = password
        customer.name = name
        session.commit()
    session.close()
