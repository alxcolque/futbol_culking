from flask import Blueprint
from app.controllers.EventController import eventcontroller
from flask_login import login_required

event_router = Blueprint('event_router', __name__)

@event_router.route('/events',methods=['GET'])
def index():
    return eventcontroller.index()

@event_router.route('/events/list',methods=['GET'])
def list():
    return eventcontroller.list()

@event_router.route('/events/create',methods=['GET'])
@login_required
def create():
    return eventcontroller.create()

@event_router.route('/events/store',methods=['POST'])
@login_required
def store():
    return eventcontroller.store()

@event_router.route('/events/store2',methods=['POST'])
@login_required
def store2():
    return eventcontroller.store2()

@event_router.route('/events/<int:id>/delete',methods=['GET'])
@login_required
def delete(id):
    return eventcontroller.delete(id)

@event_router.route('/events/<int:id>/edit',methods=['GET'])
@login_required
def edit(id):
    return eventcontroller.edit(id)

@event_router.route('/events/<int:id>/update',methods=['POST'])
@login_required
def update(id):
    return eventcontroller.update(id)

@event_router.route('/events/<int:id>/show',methods=['GET'])
@login_required
def show(id):
    return eventcontroller.show(id)