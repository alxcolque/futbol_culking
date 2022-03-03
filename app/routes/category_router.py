from flask import Blueprint
from app.controllers.CategoryController import categorycontroller

category_router = Blueprint('category_router', __name__)

@category_router.route('/categories',methods=['GET'])
def index():
    return categorycontroller.index()