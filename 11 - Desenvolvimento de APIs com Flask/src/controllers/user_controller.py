import sys
from flask import Blueprint, request

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/path/to/application/app/folder')

#import src
from src.app import User

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
    else:
        pass