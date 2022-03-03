from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from app import db
class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #FK
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(String(255))
    #Default
    created_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    #R
    