# coding : utf-8

import MySQLdb
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown') #http://192,168.1.173:8888/shutdown
def shutdown():
    shutdown_server()
    return 'Server shutting down..'

@app.route('/') #http://192.168.1.173:8888
def showall():
    db = MySQLdb.connect("localhost","root","1234","temperature")
    cur = db.cursor()
    cur.execute("select * from DHT11")

    row = cur.fetchall()
    templateData = {'data' : row}
    return render_template('temperature.html',**templateData)
    cur.close()
    db.close()
    

@app.route('/<t_hour>/<t_min>') #http://192.168.1.173:8888
def search(t_hour,t_min):
    db = MySQLdb.connect("localhost","root","1234","temperature")
    cur = db.cursor()
    sql = "select * from DHT11 where hour='%s' and min='%s'" %(t_hour,t_min)
    cur.execute(sql)

    row = cur.fetchall()
    templateData = {'data' : row}
    return render_template('temperature.html',**templateData)

    cur.close()
    db.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888,debug=True)
    
