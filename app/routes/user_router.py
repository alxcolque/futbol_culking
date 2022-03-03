from flask import Blueprint
from app.controllers.UserController import usercontroller
#from flask_login import login_required

user_router = Blueprint('user_router', __name__)

@user_router.route('/users',methods=['GET'])
def index():
    return usercontroller.index()