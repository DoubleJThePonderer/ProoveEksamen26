from flask import Flask,request, redirect, render_template, session, url_for
import mariadb
import re

app = Flask(__name__)
app.secret_key = '28ku3fl8Gq17'

def get_dbconection():
    return mariadb.connect(
    host="10.200.14.23",
    user="remoteuser",
    password="IMIKUB",
    database="spillforum"
    )

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods =['GET', 'POST'])
def login():
    mydb = get_dbconection()
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password =%s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return render_template('index.html', msg='Logged in successfully!')
        else:
            msg='Incorrect username/password'
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    mydb = get_dbconection()
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'invalid email address'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only letters and numbers'
        elif not username or not password or not email:
            msg = 'Please fill out the form'
        else:
            cursor.execute('INSERT INTO users VALUES(NULL, %s, %s, %s)', (username, password, email))
            mydb.commit()
            cursor.execute('SELECT * FROM users WHERE username = %s AND password =%s', (username, password))
            account = cursor.fetchone()
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return render_template('index.html', msg = 'you have successfully registerd')
            
    return render_template('register.html', msg=msg)

@app.route('/post', methods=['GET','POST'])
def post():
    mydb = get_dbconection()
    msg=''
    if request.method == 'POST' and 'titel' in request.form and 'content' in request.form:
        titel = request.form['titel']
        content = request.form['content']
        author = session['username']
        cursor = mydb.cursor()
        cursor.execute('INSERT INTO posts VALUES(%s,%s,%s)', (titel, content, author))
        mydb.commit()
        return render_template('index.html', msg = 'successfully posted')
        
    return render_template('post.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)