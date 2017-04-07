from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST'])
def setcookie():
    if request.method == 'POST':
        usuario = request.form['nombre']
        respuesta = make_response(render_template('readcookie.html', u=usuario))
        respuesta.set_cookie('userID', usuario)
        return respuesta

@app.route('/getcookie', methods=['POST'])
def getcookie():
    if request.method == 'POST':
        nombre = request.cookies.get('userID')
        return '<h1>Bienvenido, '+ nombre +'</h1>'
 #   nombre = request.cookies.get('userID')
 #   return '<h1>Bienvenido, '+ nombre + '</h1>'

if __name__ == "__main__":
    app.run()
