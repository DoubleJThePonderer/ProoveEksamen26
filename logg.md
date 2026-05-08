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

## 12:50
    <div class="container">
        <form action="{{ url_for('post') }}" method="post">
            <input type="text" name="titel" placeholder="titel" required>
            <input type="text" type="content" placeholder="type what ever is on your mind today" required>

            <button class="btn" type="submit"></button>
        </form>
    </div>
- post html
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
- post python

##  kilder
- https://pythonexamples.org/python-flask-if-statement-in-html-template/