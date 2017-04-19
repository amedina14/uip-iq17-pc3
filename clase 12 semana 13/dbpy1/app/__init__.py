from flask import Flask, jsonify
from app.data import obtener_empleados

app = Flask(__name__)

@app.route('/empleados')
def obtener_empleado():
    return jsonify(obtener_empleados)

if __name__=="__main__":
    app.run()

    '''lista_empleados = obtener_empleados()'''
