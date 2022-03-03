
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from app import db
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(String(50))
    description = db.Column(String(255), nullable=False)
    status = db.Column(String(50), nullable=False)
    start = db.Column(DateTime)
    end = db.Column(DateTime)
    color  = db.Column(String(30))
    #FK
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #Default
    created_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    #R