import pyowm
import json
from flask import Flask
from flask import render_template
app = Flask(__name__)

owm = pyowm.OWM('8d3023e957fcc0c9f0520b2ac4889629')

@app.route('/')
def index():
    #return '''
    #<html>
    #   <body>
    #        <h1>Hola Mundo!</h1>
    #   </body>
    #</html>
    #'''
    return render_template('index.html')

@app.route('/hola/<nombre>')
def hola_mnombre(nombre):
    return render_template('hola.html',nom=nombre)

@app.route('/vn/<int:nota>')
def validar_nota(nota):
    return render_template('validador.html',n=nota)

@app.route('/promedio')
def calcular_promedio():
    promedio = 0
    notas={'nota1':95,'nota2':75,'nota3':85}
#    print(notas.values())
    for nota in list(notas.values()):
        promedio = promedio + nota
    promedio = promedio/len(notas)
#    print(promedio)
    return render_template('promedio.html',resultado=notas, prom=promedio)


if __name__ == "__main__":
    app.run()