from ctypes import addressof
from app.models.User import User
from app.models.Client import Client
from app.models.Admin import Admin
from app import db, bcrypt, app
from flask_login import LoginManager, login_manager, login_user, logout_user, current_user
from flask import render_template, request, flash, redirect, url_for, session

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_router.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class AuthController():
    def __init__(self):
        pass
    
    def index(self):
        return render_template('welcome.html')
    
    def signup(self):
        if request.method == 'POST':
            name = request.form['nombre']
            email = request.form['email']
            username = request.form['usuario']
            password = bcrypt.generate_password_hash(request.form['password'])
            role = 'client'

            user = User(name=name, email=email, username=username, password=password,role=role)
            db.session.add(user)
            db.session.commit()

            user_id = user.id
            address = 'ninguno'
            description = 'ninguno'
            client = Client(user_id=user_id, address=address, description=description)
            db.session.add(client)
            db.session.commit()

            flash('Usuario registrado exitosamente')
            return render_template('auth/login.html')
        return render_template('auth/signup.html')

    def login(self):
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user:
                if bcrypt.check_password_hash(user.password, request.form['password']):
                        login_user(user)
                        if user.role == 'admin':
                            return redirect(url_for('welcome_router.admin'))
                        else:
                            return redirect(url_for('welcome_router.client'))
                        
            
            flash('Usuario no existe, o los creadenciales no son válidos')
            return redirect(url_for('welcome_router.index'))
        return render_template('auth/login.html')
    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('auth_router.main'))

authcontroller = AuthController()