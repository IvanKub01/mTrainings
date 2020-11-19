from flask import Flask, render_template, session, request , jsonify
from flask_sqlalchemy import SQLAlchemy
from requests import Session
from model import *
from function import *
from datetime import date, datetime, timedelta
from flask_marshmallow import Marshmallow
import pyodbc
import json
import re
from sqlalchemy import func
import string
app = Flask(__name__)
ma = Marshmallow(app)
app.config.from_pyfile('config/config.py')
app.secret_key = 'some secret key'
db = SQLAlchemy(app)

# THIS SHOULD PREVENT CACHING OF CSS AND JS FILES
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r 
@app.route('/domovhtml', methods=['GET', 'POST'])
def domovhtml():
    return render_template("Chp1.html")


@app.route('/otvaraciehodiny', methods=['GET', 'POST'])
def otvaraciehodiny():
    return render_template("Chp2.html")

@app.route('/kontakthmtl', methods=['GET', 'POST'])
def kontakthmtl():
    return render_template("Chp3.html")
@app.route('/datahmtl', methods=['GET', 'POST'])
def datahmtl():
    return render_template("Chp4.html")
@app.route('/edithmtl', methods=['GET', 'POST'])
def edithmtl():
    return render_template("Chp5.html")
# MAIN PAGE - root of server, for example localhost:5102
@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template("Chp1.html") #,listofNamesZod = listOfNamesZod)
@app.route('/insertNick', methods=['POST'])
def insertNick():
    x = request.form['idNick'].strip()
    y = request.form['IDpass'].strip()

    nicky = zoznam(nick=x,password=y)
    db.session.add(nicky)
    db.session.commit()
    
    return x 


@app.route('/readNick', methods=['GET'])
def read():
    idNick = request.args.get('idNick')
    

    udajeZam = db.session.query(zoznam).filter(zoznam.nick==idNick).first()
    data = zoznamSchema(many=False).dump(udajeZam)    
    print(data)
    res = not bool(data) 
    print("Is dictionary empty ? : " + str(res)) 
    print(type(data))
    return jsonify(data)


@app.route('/printZoznam', methods=['GET'])
def printZoznam():

    Nazov = request.args.get('idd')
    print(Nazov)
    result = db.session.execute("SELECT idcko ,nick ,password FROM zoznam")
    result = [dict(row) for row in result]
    print(result)    

    
    return json.dumps(result)


@app.route('/delIDfun', methods=['DELETE'])
def delIDfun():
    xq = request.form['delID'].strip()
    # print(xq)

    delfun = db.session.query(zoznam).filter_by(idcko = xq).first()
    db.session.delete(delfun)
    
    db.session.commit()
    data = zoznamSchema(many=False).dump(delfun)
   
    return jsonify(data)
   
# # +++++++++++++++++++++++++++++++++++++++++++++++++delete++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@app.route('/updateTerm', methods=['PUT'])
def updateTerm():  
    nick1 = request.form['nick'].strip()
    password1 = request.form['password'].strip()
    idcko1 = request.form['id'].strip()
    
    
    
    
    print(idcko1," ",password1," ",nick1," ")

    

    updateT = db.session.query(zoznam).get(idcko1)
    updateT.password = password1
    updateT.nick = nick1
    

    db.session.commit()


    return idcko1
 
# +++++++++++++++++++++++++++++++++++++++++++++++++main++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'memcached'
    sess = Session()
  
    app.debug = True
    app.run(threaded=True, host='localhost', port=5106)
    

# endregion
