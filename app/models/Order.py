
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from app import db
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(String(30))
    total = db.Column(db.Numeric(10,2))
    #FK
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    #Default
    created_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    #R