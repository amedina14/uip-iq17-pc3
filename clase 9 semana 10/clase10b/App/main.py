from flask import Flask
from flask import request
from flask import render_template

App=Flask(__name__)

@App.route('/')
def circuferencia():
    return render_template('cincunferencia.html')

@App.route('/resultado', methods=['POST'])
def resultado():
    if request.method=='POST':
        radio=float(request.form.get("radio"))
        resultado=radio*radio*3.1416
        return render_template('area.html', re=resultado,ra=radio)

if __name__=="__main__":
    App.run()