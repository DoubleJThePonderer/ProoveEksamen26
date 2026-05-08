## 11:43
    cursor.execute('SELECT * FROM users WHERE username = %s AND password =%s', (username, password))
    account = cursor.fetchone()
    session['loggedin'] = True
    session['id'] = account[0]
    session['username'] = account[1]
    return render_template('index.html', msg = 'you have successfully registerd')
-det var det jeg skrev  til å skape inlogging da du har registrert

## 12:31
    <header>
        {% if session['loggedin'] == True: %}
        <h1>{{  session.username }}</h1>
        <input type="text">
        <a href="{{ url_for('logout') }}">log out</a>
        {% else %}
        <h1>logged out</h1>
        <input type="text">
        <a href="{{ url_for('login') }}">log in</a>
        {% endif %}
    </header>
- lagde en top bar for index intill videre

## 12:38
- gjorde idex til root side
- lagde links mellom login, register og index

## 

##  kilder
- https://pythonexamples.org/python-flask-if-statement-in-html-template/