#producto
from typing import Text
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from app import db
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #FK
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    product = db.Column(String(100))
    price = db.Column(db.Numeric(10,2))
    promo = db.Column(db.Numeric(10,2))
    description = db.Column(db.Text)
    img_url = db.Column(String(150))
    #Default
    created_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    
    #R
    #category = db.relationship("Category", backref='productos', lazy='dynamic')
    order = db.relationship(
        'OrderDetail', backref='product', lazy='dynamic')
    