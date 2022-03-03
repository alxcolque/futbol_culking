__version__ = "0.1"
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import app.config
from flask_bcrypt import Bcrypt
from app.config import (_db_user, _db_pass, _db_host,_db_name, _os_path)
import secrets

#
UPLOAD_FOLDER = 'app/static/img/'
OS_PAHT = _os_path 

app = Flask(__name__, template_folder="views")

#configuraciones base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', _db_user),
    os.getenv('DB_PASSWORD', _db_pass),
    os.getenv('DB_HOST', _db_host),
    os.getenv('DB_NAME', _db_name)
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret

app.debug = True

#rutas
from app.routes.welcome_router import welcome_router
app.register_blueprint(welcome_router)

from app.routes.auth_router import auth_router
app.register_blueprint(auth_router)

from app.routes.event_router import event_router
app.register_blueprint(event_router)

from app.routes.user_router import user_router
app.register_blueprint(user_router)

from app.routes.product_router import product_route
app.register_blueprint(product_route)

from app.routes.category_router import category_router
app.register_blueprint(category_router)

from app.routes.order_router import order_router
app.register_blueprint(order_router)