from app.models.User import User
from app import db
from flask import render_template, flash, redirect, url_for, request
class UserController():
    def __init__(self):
        pass

    def index(self):
        # usuario = {'name': 'Josam Pinaya'}
        usuarios= User.query.all()
        return render_template('users/index.html', users=usuarios)
        """ from app.models.Usuario import Usuario
        usuarios = User.query.all()
        return render_template('materias/index.html', usuarios=usuarios) """
    def eliminar(self, _id):
        usuario = User.query.get(_id)
        db.session.delete(usuario)
        db.session.commit()
        flash('El usuario '+ usuario.nombre +' se ha eliminado con éxito.')
        return redirect(url_for('usuario_route.index'))
    def obtenerUsuario(self, _id):
        consulta_rol =  User.query.get(_id)
        return str(consulta_rol.rol_usuario)
    def cambiarRol(self):
        if request.method == 'POST':
            rol_usuario = request.form['rol']
            _id = request.form['id']
            usuario = User.query.get(_id)
            usuario.rol_usuario = rol_usuario
            db.session.commit()
            flash('El usuario '+ usuario.nombre +' ahora es '+ rol_usuario)
            return redirect(url_for('usuario_route.index'))
usercontroller = UserController()