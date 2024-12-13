from http import HTTPStatus

from flask import Blueprint, request
from app import User, db

app = Blueprint('user', __name__, url_prefix='/users')


def _create_user():
    data = request.json
    user = User(username=data['username'])
    db.session.add(user)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def handle_user():
    if request.method == 'GET':
        _create_user()
        return {'message': 'User successfully created'}, HTTPStatus.CREATED
    else:
        return {'users': []}