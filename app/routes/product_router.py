from flask import Blueprint
from app.controllers.ProductController import productcontroller

product_route = Blueprint('product_route', __name__)

@product_route.route('/products',methods=['GET'])
def index():
    return productcontroller.index1()

@product_route.route('/products/create',methods=['GET'])
def create():
    return productcontroller.create()

@product_route.route('/products/store',methods=['POST'])
def store():
    return productcontroller.store()

@product_route.route('/products/<int:id>/delete',methods=['GET'])
def delete(id):
    return productcontroller.delete(id)

@product_route.route('/products/<int:id>/edit',methods=['GET'])
def edit(id):
    return productcontroller.edit(id)

@product_route.route('/products/<int:id>/update',methods=['POST'])
def update(id):
    return productcontroller.update(id)

@product_route.route('/products/<int:id>/show',methods=['GET'])
def show(id):
    return productcontroller.show(id)

@product_route.route('/products/torta',methods=['GET'])
def torta():
    return productcontroller.torta()

@product_route.route('/products/masita',methods=['GET'])
def masita():
    return productcontroller.masita()
@product_route.route('/products/pan',methods=['GET'])
def pan():
    return productcontroller.pan()