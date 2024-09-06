#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Float
from models.base import Base, Session

class Product(Base):
    __tablename__ = 'products'
    id = Column(String, primary_key=True)
    name = Column(String)
    brand = Column(String)
    size = Column(String)
    price = Column(Float)
    additional_info = Column(String)
    quantity = Column(Integer)

def add_product(name, brand, size, price, additional_info, quantity):
    session = Session()
    product_id = f"{name}-{size}"
    if session.query(Product).filter_by(id=product_id).first():
        print("Product already exists.")
        return
    new_product = Product(id=product_id, name=name, brand=brand, size=size, price=price, additional_info=additional_info, quantity=quantity)
    session.add(new_product)
    session.commit()
    session.close()

def update_product(name, brand, size, price, additional_info):
    session = Session()
    product_id = f"{name}-{size}"
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        product.brand = brand
        product.price = price
        product.additional_info = additional_info
        session.commit()
    session.close()
