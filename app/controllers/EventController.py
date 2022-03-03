from http.client import HTTPResponse
from app.models.Event import Event
from app.models.User import User
from app import db
from flask import render_template, flash, redirect, url_for, request, jsonify, Response
from flask_login import current_user
import json
from json import JSONEncoder
class EventController():
    def __init__(self):
        pass

    def index(self):
        # usuario = {'name': 'Josam Pinaya'}
        events= Event.query.all()
        return render_template('events/index.html', events=events)

    def list(self):
        #people = [{'title': 'Alice', 'start':'Tue, 01 Mar 2022 11:37:00 GMT', 'end':'Tue, 01 Mar 2022 11:37:00 GMT'},
          #{'title': 'Bob', 'start':'Tue, 01 Mar 2022 11:37:00 GMT', 'end':'Tue, 01 Mar 2022 11:37:00 GMT'}]
        #return jsonify(people)
        #events = {'title': 'Josam Pinaya', 'start':'Tue, 01 Mar 2022 11:37:00 GMT', 'color':'red'}
        events= db.session.query(Event.id, Event.title, Event.description, Event.start, Event.end , Event.color).all()
        #events= User.query.all()
        payload = []
        content = {}
        for result in events:
            content = {
                'id': result[0], 
                'title': result[1], 
                'description': result[2], 
                'start': str(result[3]),
                'end': str(result[4]),
                'color': str(result[5]),
            }
            payload.append(content)
            content = {}
        return jsonify(payload)
        #events = Event.query.all()

        
        #return ls
        #return db.session.query(Event.title, Event.start, Event.color).all()
        #res = json.dumps (events)
        #return res

    def store(self):

        if request.method == 'POST':
            try:
                title = request.form['title']
                description = request.form['description']
                start = request.form['start']
                end = request.form['end']
                color = request.form['color']
                status = 1
                user_id = current_user.id

                event = Event(title=title, description=description,start=start, end=end, color=color, user_id=user_id, status=status)
                db.session.add(event)
                db.session.commit()
                msg = {'estado': '1', 'msg': 'Registro realizado con exito', 'tipo':'success'}
                return json.dumps(msg)
            except Exception as e:
                return json.dumps(400, "Exception: %s" % e).payload()
        msg = {'estado': '0', 'msg': 'Error al registrar', 'tipo':'error'}
        return json.dumps(msg)
    def store2(self):

        if request.method == 'POST':
            try:
                title = request.form['title']
                description = request.form['description']
                start = request.form['start']
                end = request.form['end']
                color = request.form['color']
                status = 1
                user_id = current_user.id

                event = Event(title=title, description=description,start=start, end=end, color=color, user_id=user_id, status=status)
                db.session.add(event)
                db.session.commit()
                flash('Horario reservado con éxito')
                return redirect(url_for('welcome_router.index'))
            except Exception as e:
                return json.dumps(400, "Exception: %s" % e).payload()
        msg = {'estado': '0', 'msg': 'Error al registrar', 'tipo':'error'}
        return json.dumps(msg)
            
    def delete(self, _id):
        event = Event.query.get(_id)
        db.session.delete(event)
        db.session.commit()
        return 'ok'
    def obtenerUsuario(self, _id):
        consulta_rol =  Event.query.get(_id)
        return str(consulta_rol.rol_usuario)
    def cambiarRol(self):
        if request.method == 'POST':
            rol_usuario = request.form['rol']
            _id = request.form['id']
            usuario = Event.query.get(_id)
            usuario.rol_usuario = rol_usuario
            db.session.commit()
            flash('El usuario '+ usuario.nombre +' ahora es '+ rol_usuario)
            return redirect(url_for('usuario_route.index'))
eventcontroller = EventController()
