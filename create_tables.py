#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.admin import Admin
from models.customer import Customer
from models.deliverer import Deliverer
from models.product import Product
from models.cart import Cart
from models.order import Order
from models.engine.database import Base

# Replace 'sqlite:///your_database.db' with your actual database URL
DATABASE_URL = 'sqlite:///your_database.db'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

print("Tables created successfully.")
