from flask import Blueprint
from app.controllers.OrderController import ordercontroller
from flask_login import login_required

order_router = Blueprint('order_router', __name__)

@order_router.route('/orders',methods=['GET'])
@login_required
def index():
    return ordercontroller.index()

@order_router.route('/client/micarrito',methods=['GET','POST'])
@login_required
def carrito():
    return ordercontroller.carrito()

@order_router.route('/client/micarrito/quitar/<int:id>',methods=['GET'])
@login_required
def quitar(id):
    return ordercontroller.quitar(id)

@order_router.route('/orders/aceptar/<int:id>',methods=['GET'])
@login_required
def aceptar(id):
    return ordercontroller.aceptar(id)

@order_router.route('/orders/rechazar/<int:id>',methods=['GET'])
@login_required
def rechazar(id):
    return ordercontroller.rechazar(id)