from flask import session
from app import db, bcrypt, app
from app.models.Category import Category
from app.models.User import User
from app.models.UserPhoto import UserPhoto
from app.models.Event import Event
from app.models.Product import Product
from app.models.Admin import Admin
from app.models.Client import Client
from app.models.Order import Order
from app.models.ProductPhoto import ProductPhoto
from app.models.OrderDetail import OrderDetail




def insertUser():
    #from sqlalchemy import func
    #user_id = session.query(func.max(User.id)).scalar()
    id = 1

    name = 'Don Juan'
    username = 'admin'
    email = 'admin@admin.com'
    password = bcrypt.generate_password_hash('ñlkjhgfd')
    photo = 'user.png'
    role = 'admin'

    user = User(id=id, name=name,username=username,email=email, password=password, photo=photo, role=role)
    db.session.add(user)
    db.session.commit()

    description = 'a'
    admin = Admin(description=description,user_id=id)
    db.session.add(admin)
    db.session.commit()
    
db.drop_all()
db.create_all()
insertUser()
