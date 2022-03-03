from app.models.Client import Client
from flask import render_template, url_for, request, redirect, flash, jsonify
from app.models.Order import Order
from app.models.OrderDetail import OrderDetail
from app.models.Product import Product
from app.models.User import User
from flask_login import login_user, logout_user, current_user
from sqlalchemy import or_
from app import db


class OrderController():
    def __init__(self):
        pass
    #client
    def carrito(self):
        user_id = current_user.id
        if request.method == 'POST':
            #si existe producto y usuario entonces: actualiar 
            # sino crear 
            

            #Agregar pedido
            id = request.form['id']
            status = 1 #pedido
            prod_id = id
            producto = Product.query\
            .filter(Product.id == id)\
            .first()

            total = producto.price

            client = Client.query\
            .filter(Client.user_id == user_id)\
            .first()

            client_id = client.id
            
            est_pedido = Order(status=status, total=total, client_id=client_id)
            db.session.add(est_pedido)
            db.session.commit()

            order_id = est_pedido.id
            product_id = prod_id
            quantity = 1
            orderDetail = OrderDetail(order_id=order_id,product_id=product_id,quantity=quantity)
            db.session.add(orderDetail)
            db.session.commit()
            return jsonify(results=user_id)
        return 1
        carrito = Order.query\
            .join(Product, Product.id==Order.prod_id)\
            .join(User, Order.user_id==User.id)\
            .filter(or_(Order.estado == 2, Order.estado == 3))\
            .filter(User.id == user_id)\
            .all()
            #.add_columns(Pedido.prod_id)\
        total = db.session.query(db.func.sum(Order.subtotal))\
            .filter(or_(Order.estado == 2, Order.estado == 3))\
            .scalar()
        return render_template('clients/micarrito.html', carrito=carrito, total=total)
    def quitar(self, _id):
        pedido =  Order.query.get(_id)   
        db.session.delete(pedido)
        db.session.commit()
        flash('El producto quitado de carrito.')

    #admin
    def index(self):
        #pedidos = Pedido.query.join(Usuario).filter_by(rol_usuario='cliente').all()
        pedidos = OrderDetail.query\
            .join(Product, Product.id==OrderDetail.product_id)\
            .all()
        return render_template('orders/index.html', pedidos=pedidos)
    def aceptar(self, _id):
        pedido =  Order.query.get(_id)
        pedido.status = 4
        db.session.commit()
        return redirect(url_for('pedido_router.index'))
    def rechazar(self, _id):
        pedido =  Order.query.get(_id)
        pedido.status = 5
        db.session.commit()
        return redirect(url_for('pedido_router.index'))
    
            
ordercontroller = OrderController()