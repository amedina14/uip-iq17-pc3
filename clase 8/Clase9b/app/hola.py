#redirect, url_for: librerias de flask importantes
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/admin')
def hola_admin():
    return 'Eres un administrador'

@app.route('/invitado/<invitado>')
def hola_invitado(invitado):
    return 'Bienvenido, %s, eres un invitado' % invitado

@app.route('/usuario/<nombre>')
def hola_usuario(nombre):
    if nombre == "admin":
        return redirect(url_for('hola_admin'))
    else:
        return redirect(url_for('hola_invitado', invitado=nombre))
#rutas index
@app.route('/')
def hola_mundo():
    return 'Hola UIP'

#rutas 2
@app.route('/relajo')
def relajo():
    return 'Relajo'

#rutas pasando parametro <nombre>. Metodo Get
@app.route('/hola/<nombre>')
def hola_nombre(nombre):
    return 'Hola %s!' % nombre

#rutas pasando parametro int <edad>. Metodo Get
@app.route('/edad/<int:edad>')
def validar_votacion(edad):
    if edad > 18:
      return 'puede votar'
    else:
      return 'no puede votar'

#rutas pasando parametro float <radio>. Metodo Get
@app.route('/circulo/<float:radio>')
def calcular_area(radio):
    return 'El area del circulo es: %f cm' % (3.1416*radio*radio)

@app.route('/exito/<nombre>')
def exito(nombre):
    return 'Bienvenido %s' % nombre

#ruta para el Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['nombre']
        return redirect(url_for('exito',nombre=usuario))
    else:
        usuario = request.args.get('nombre')
        return redirect(url_for('exito',nombre=usuario))

if __name__=="__main__":
    app.run()
