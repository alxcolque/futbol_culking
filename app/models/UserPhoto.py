
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from app import db
class UserPhoto(db.Model):
    __tablename__ = 'user_photos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #FK
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    url = db.Column(db.String(150))
    created_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    #R