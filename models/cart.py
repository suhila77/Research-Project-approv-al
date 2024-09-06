#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Float
from models.base import Base, Session

class Cart(Base):
    __tablename__ = 'carts'
    customer_id = Column(Integer, primary_key=True)
    product_id = Column(String, primary_key=True)
    product_price = Column(Float)
    quantity = Column(Integer)

def add_to_cart(customer_id, product_id, quantity):
    session = Session()
    existing_cart_item = session.query(Cart).filter_by(customer_id=customer_id, product_id=product_id).first()
    if existing_cart_item:
        existing_cart_item.quantity += quantity
    else:
        product_price = session.query(Product).filter_by(id=product_id).first().price
        new_cart_item = Cart(customer_id=customer_id, product_id=product_id, product_price=product_price, quantity=quantity)
        session.add(new_cart_item)
    session.commit()
    session.close()

def remove_from_cart(customer_id, product_id, quantity):
    session = Session()
    cart_item = session.query(Cart).filter_by(customer_id=customer_id, product_id=product_id).first()
    if cart_item:
        if cart_item.quantity > quantity:
            cart_item.quantity -= quantity
        else:
            session.delete(cart_item)
        session.commit()
    session.close()
