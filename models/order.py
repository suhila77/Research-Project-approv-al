#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.sql import func
from models.base import Base, Session

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer)
    total_price = Column(Float)
    date_time = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Enum('pending', 'ready', 'delivered'))

def place_order(customer_id):
    session = Session()
    # Retrieve items from the cart
    cart_items = session.query(Cart).filter_by(customer_id=customer_id).all()
    total_price = sum(item.product_price * item.quantity for item in cart_items)
    
    new_order = Order(customer_id=customer_id, total_price=total_price, status='pending')
    session.add(new_order)
    session.commit()
    
    # Remove items from the cart
    for item in cart_items:
        session.delete(item)
    session.commit()
    
    session.close()
    return new_order.id

def cancel_order(order_id):
    session = Session()
    order = session.query(Order).filter_by(id=order_id).first()
    if order and order.status == 'pending':
        session.delete(order)
        session.commit()
    session.close()

def order_ready(order_id):
    session = Session()
    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        order.status = 'ready'
        session.commit()
    session.close()

def order_shipping(order_id):
    session = Session()
    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        order.status = 'shipping'
        session.commit()
    session.close()

def order_delivered(order_id):
    session = Session()
    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        order.status = 'delivered'
        session.commit()
    session.close()
