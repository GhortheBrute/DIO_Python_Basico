from flask import Flask, url_for

app = Flask(__name__)

@app.route('/olamundo/<usuario>/<int:idade>/<float:altura>')
def hello_world(usuario, idade, altura):
    return {
        'usuário': usuario,
        'idade': idade,
        'altura': altura
    }

@app.route('/bemvindo')
def bem_vindo():
    return {"message": "Olá mundo!"}

@app.route('/projects/')
def projects():
    return f"<h1>Projects</h1>"

@app.route('/about')
def about():
    return f"<h1>About</h1>"

with app.test_request_context():
    url = '/about'
    print(url_for('hello_world', usuario="John Doe", idade=35, altura=1.74))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('bem_vindo'))
