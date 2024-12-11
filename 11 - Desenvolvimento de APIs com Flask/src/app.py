from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/bemvindo/<usuario>/<int:idade>/<float:altura>')
def bem_vindo(usuario, idade, altura):
    print(idade)
    print(altura)
    return f"<h1>Bem, vindo {usuario}!</h1>"

@app.route('/projects/')
def projects():
    return f"<h1>Projects</h1>"

@app.route('/about')
def about():
    return f"<h1>About</h1>"

with app.test_request_context():
    url = '/about'
    print(url_for('index'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('bem_vindo', usuario="John Doe", idade=35, altura=1.74))
