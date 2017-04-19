import pyowm
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
import sqlite3


app = Flask(__name__)

owm = pyowm.OWM('8d3023e957fcc0c9f0520b2ac4889629')

@app.route('/')
def index():
#    if request.method == 'POST':
        return render_template('pgsup.html')


@app.route('/meteo', methods=['POST'])
def meteo():
    if request.method == 'POST':

        city = request.form['ciudad']

        observation = owm.weather_at_place(city)#["reception time"]
        w = observation.get_weather()

        l = observation.get_location()
        lugar = l.get_country()
        place = l.get_name()
        sunset = w.get_sunset_time('iso')
        status = w.get_detailed_status()
        viento = w.get_wind()["speed"]
        degradacion = w.get_wind()["deg"]
        humedad = w.get_humidity()
        press = w.get_pressure()['press']
        lvmar = w.get_pressure()['sea_level']
        temp = w.get_temperature('celsius')["temp"]

        return render_template('meteo.html', ciudad=city, observacion=observation, sunset=sunset, press=press, lvmar=lvmar,
                               clima=status, viento=viento, humedad=humedad, temp=temp, degradacion=degradacion,
                               lugar=lugar, place=place)

#ruta para el Login
@app.route('/login')
def paglogin():
        return render_template('login.html')


@app.route('/validarLogin', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('campousuario')
        campopassword = request.form.get('campopassword')
        return render_template('pglogeado.html',nombre=usuario, campopassword=campopassword)
    else:
        usuario = request.args.get('campousuario')
        campopassword = request.form.get('campopassword')
        return render_template('pglogeado.html',nombre=usuario, campopassword=campopassword)

@app.route('/reg')
def pagregistrate():
        return render_template('registrate.html')

@app.route('/Registrate', methods=['POST', 'GET'])
def Registrate():
    if request.method == 'POST':
        usuario = request.form.get('campousuario')
        mail = request.form.get('mail')
        campopassword = request.form.get('campopassword')
        return render_template('pgregistrado.html', nombre=usuario, mail=mail,campopassword=campopassword)


if __name__ == "__main__":
    app.run(debug=True)



