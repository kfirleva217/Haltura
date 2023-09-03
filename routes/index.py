import hashlib

from app import app, mysql
from flask import render_template, request, redirect, url_for, session


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT username, password, user_type FROM client WHERE username = %s", (username,))
        client = cur.fetchone()

        if not client:
            cur.execute("SELECT username, password, user_type FROM handyman WHERE username = %s", (username,))
            handyman = cur.fetchone()
            cur.close()

            if handyman and handyman[1] == hashlib.sha256(password.encode()).hexdigest():
                session['username'] = handyman[0]
                session['user_type'] = handyman[2]
                return redirect(url_for('profile'))
            else:
                return "Invalid credentials. Please try again."
        else:
            cur.close()
            if client and client[1] == hashlib.sha256(password.encode()).hexdigest():
                session['username'] = client[0]
                session['user_type'] = client[2]
                return redirect(url_for('profile'))
            else:
                return "Invalid credentials. Please try again."

    # Add a return statement in case the request method is GET
    return render_template('login.html')


@app.route('/profile')
def profile():
    user_id = 1
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM handyman WHERE user_id = {user_id}")
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return render_template('profile.html', user=user)
    else:
        return "User not found"


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_type = request.form['user-type']
        conn = mysql.connection
        cursor = conn.cursor()
        if user_type == 'handyman':
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            state = request.form['state']
            full_name = request.form['full-name']
            about_yourself = request.form['about-yourself']
            occupation = request.form.get('occupation', None)
            experience = request.form.get('experience', None)
            sql = f"INSERT INTO handyman (email, username, password, state, occupation, experience, full_name, about_yourself) VALUES ('{email}', '{username}', '{password}', '{state}', '{occupation}', '{experience}', '{full_name}', '{about_yourself}')"
        else:
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            state = request.form['state']
            print('2')
            sql = f"INSERT INTO clients (email, username, password, state) VALUES ('{email}', '{username}', '{password}', '{state}')"

        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('profile'))

    return render_template('signup.html')
