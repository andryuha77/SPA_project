# Originally adapted from:
# http://flask.pocoo.org/
# https://github.com/mjhea0/thinkful-mentor/tree/master/python/jinja/flask_example
# https://github.com/ihoegen/Flask-Login-App-Tutorial

from flask import Flask, Flask, render_template, redirect, url_for, request, g
import datetime
import sqlite3
import hashlib
from time import sleep

import flask as fl
app = fl.Flask(__name__)

# Originally adapted from:
# https://github.com/ihoegen/Flask-Login-App-Tutorial

def insertUser(username,password):
    con = sqlite3.connect("static/user.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Users")
        rows = cur.fetchall()
        for row in rows:
            dbUser = row[0]
            dbPass = row[1]
            if dbUser==username and dbPass==password:
                completion=True
    return completion


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('start'))
    return render_template('login.html', error=error, current_time=datetime.datetime.now())



@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = insertUser(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('start'))
    return render_template('register.html', error=error, current_time=datetime.datetime.now())



@app.route('/start', methods=['GET', 'POST'])
def start():
    return render_template('template.html', current_time=datetime.datetime.now())


@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

#Originally adapted from:
#http://flask.pocoo.org/docs/0.11/quickstart/
@app.route("/result", methods=['GET', 'POST'])
@app.route('/result/<name>')
def result(name=None):
    return render_template('result.html',title="Advise from ", name=fl.request.form["name"], current_time=datetime.datetime.now())
 
@app.route("/about")
def about():
    return render_template('template.html', my_string="Bar", 
    title="About", current_time=datetime.datetime.now())


#include debuger
if __name__ == '__main__':
    app.run(debug=True)
