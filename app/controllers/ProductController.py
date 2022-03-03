from unicodedata import category
from flask import render_template, url_for, request, redirect, flash
from app.models.Product import Product
from app.models.Category import Category
from app import db, app

import os
import time
from PIL import Image #pip install pillow
import urllib.request
from werkzeug.utils import secure_filename

class ProductController():
    def __init__(self):
        pass

    def index1(self):
        producto = Product.query.all()
        return render_template('products/list.html',producto=producto)
    def create(self):
        categories = Category.query.all()
        return render_template('products/create.html', categories=categories)
    def store(self):
        if request.method == 'POST':
            product = request.form['product']
            price = request.form['price']
            description = request.form['description']
            category_id = request.form['category_id']
            promo = 0
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
            if file: #and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                #guardar nombre
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
                fecha = time.strftime("%Y%m%d%H%M%S")
                imgPath = app.config['UPLOAD_FOLDER'] + filename
                img = Image.open(imgPath)
                img.save('app/static/img/'+fecha+'.png')
                os.remove('app/static/img/'+filename)
                newfilename = fecha+'.png'
                
                
                productoadd = Product(product = product,price=price,description=description,img_url=newfilename,category_id=category_id,promo=promo)
                db.session.add(productoadd)
                db.session.commit()

                
                
                flash('El registro se ha realizado con éxito.')
                return redirect(url_for('product_route.index'))
            else:
                flash('Allowed image types are -> png, jpg, jpeg, gif')
                return redirect(request.url)
            
    def delete(self, _id):
        producto = Product.query.get(_id)
        db.session.delete(producto)
        db.session.commit()
        flash('El registro se ha eliminado con éxito.')
        return redirect(url_for('product_route.index'))
    def edit(self, _id):
        product = Product.query.get(_id)
        return render_template('products/edit.html',product=product)
    def update(self, _id):
        if request.method == 'POST':
            v_nom_prod = request.form['product']
            v_precio = request.form['price']
            v_desc_prod = request.form['description']

            producto =  Product.query.get(_id) 
            producto.product = v_nom_prod
            producto.price = v_precio
            producto.description = v_desc_prod

            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                #flash('No image selected for uploading')
                
                db.session.commit()
                flash('El producto se ha actualizado con éxito.')
                return redirect(url_for('product_route.index'))
            if file: #and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                #guardar nombre
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
                fecha = time.strftime("%Y%m%d%H%M%S")
                imgPath = app.config['UPLOAD_FOLDER'] + filename
                img = Image.open(imgPath)
                img.save('app/static/img/'+fecha+'.png')
                os.remove('app/static/img/'+filename)
                newfilename = fecha+'.png'

                producto =  Product.query.get(_id)   
                producto.img_url = newfilename
                db.session.commit()
                flash('El producto se ha actualizado con éxito.')
                return redirect(url_for('product_route.index'))
            else:
                flash('Allowed image types are -> png, jpg, jpeg, gif')
                return redirect(request.url)
    def show(self, _id):
        product = Product.query.get(_id)
        return render_template('products/show.html',product=product)  

    def torta(self):
        producto = Product.query.filter_by(tipo = 'torta').all()
        return render_template('producto/tortas.html',producto=producto)    
    def masita(self):
        producto = Product.query.filter_by(tipo = 'masita').all()
        return render_template('producto/masitas.html',producto=producto) 
    def pan(self):
        producto = Product.query.filter_by(tipo = 'pan').all()
        return render_template('producto/panes.html',producto=producto)   
        
productcontroller = ProductController()