#!/usr/bin/python3

from sqlalchemy import Column, String
from models.base import Base, Session

class Admin(Base):
    __tablename__ = 'admins'
    email = Column(String, primary_key=True)
    password = Column(String)
    name = Column(String)

def add_admin(email, password, name):
    session = Session()
    if session.query(Admin).filter_by(email=email).first():
        print("Admin already exists.")
        session.close()
        return
    new_admin = Admin(email=email, password=password, name=name)
    session.add(new_admin)
    session.commit()
    session.close()

def update_admin(email, password, name):
    session = Session()
    admin = session.query(Admin).filter_by(email=email).first()
    if admin:
        admin.password = password
        admin.name = name
        session.commit()
    session.close()
