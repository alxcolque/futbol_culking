from app.models.Category import Category
from app import db
from flask import render_template, flash, redirect, url_for, request
class CategoryController():
    def __init__(self):
        pass

    def index(self):
        # usuario = {'name': 'Josam Pinaya'}
        categories= Category.query.all()
        return render_template('categories/index.html', categories=categories)
    def eliminar(self, _id):
        usuario = Category.query.get(_id)
        db.session.delete(usuario)
        db.session.commit()
        flash('El usuario '+ usuario.nombre +' se ha eliminado con éxito.')
        return redirect(url_for('usuario_route.index'))
    
categorycontroller = CategoryController()