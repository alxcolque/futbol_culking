from flask import Blueprint
from app.controllers.WelcomeController import welcomecontroller
#from flask_login import login_required

welcome_router = Blueprint('welcome_router', __name__)

@welcome_router.route('/',methods=['GET'])
def index():
    return welcomecontroller.index()
@welcome_router.route('/',methods=['GET'])
def client():
    return welcomecontroller.client()
@welcome_router.route('/admin',methods=['GET'])
def admin():
    return welcomecontroller.admin()