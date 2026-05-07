from flask import Flask,request, redirect, render_template, session, url_for
import mysql.connector
import re

app = Flask(__name__)
app.secret_key = '28ku3fl8Gq17'

def get_dbconection():
    return mysql.connector.connect(
    host="",
    user="",
    password="IMIKUB",
    database=""
    )

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    mydb = get_dbconection()
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password =%s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return render_template('index.html', msg='Logged in successfully!')
        else:
            msg='Incorrect username/password'
    return render_template('login.html', msg=msg)