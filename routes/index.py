import hashlib

from app import app, mysql
from flask import render_template, request, redirect, url_for, session, flash


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user-type']
        email = request.form['email']
        password = request.form['password']
        if user_type == 'client':
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM clients WHERE email = %s", (email,))
            userAttempt = cur.fetchone()
            cur.close()
            if userAttempt:
                if userAttempt[2] == password:
                    return render_template("home.html")
                else:
                    flash('The password is incorrect, please try again',category='Error')
                    return render_template("login.html")
            else:
                flash('The username is incorrect, please try again', category='Error')
            # return render_template("login.html")
        if user_type == 'handyman':
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM handyman WHERE email = %s", (email,))
            userAttempt = cur.fetchone()
            cur.close()

            if userAttempt:
                if userAttempt[4] == password:
                    return render_template("home.html")
                else:
                    flash('The password is incorrect, please try again',category='Error')
                    return render_template("login.html")
            else:
                flash('The username is incorrect, please try again', category='Error')
    return render_template("login.html")
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT username, password, user_type FROM client WHERE username = %s", (username,))
#         client = cur.fetchone()
#
#         if not client:
#             cur.execute("SELECT username, password, user_type FROM handyman WHERE username = %s", (username,))
#             handyman = cur.fetchone()
#             cur.close()
#
#             if handyman and handyman[1] == hashlib.sha256(password.encode()).hexdigest():
#                 session['username'] = handyman[0]
#                 session['user_type'] = handyman[2]
#                 print('aa')
#                 return render_template('profile.html',)
#             else:
#                 print('bb')
#                 return "Invalid credentials. Please try again."
#         else:
#             cur.close()
#             if client and client[1] == hashlib.sha256(password.encode()).hexdigest():
#                 session['username'] = client[0]
#                 session['user_type'] = client[2]
#                 print('cc')
#                 return render_template('profile.html',)
#             else:
#                 print('dd')
#                 return "Invalid credentials. Please try again."
#         print('ff')
#     # Add a return statement in case the request method is GET
#     return render_template('login.html')


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
        sql="";
        if user_type == 'handyman':
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            state = request.form['state']
            full_name = request.form['full-name']
            about_yourself = request.form['about-yourself']
            occupation = request.form.get('occupation', None)
            experience = request.form.get('experience', None)
            if cursor.execute("SELECT * FROM handyman WHERE username =%s", (username,)):
                flash("the username is already exists")
            else:
                sql = f"INSERT INTO handyman (email, username, password, state, occupation, experience, full_name, about_yourself) VALUES ('{email}', '{username}', '{password}', '{state}', '{occupation}', '{experience}', '{full_name}', '{about_yourself}')"
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for('login'))
        else:
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            state = request.form['state']
            if cursor.execute("SELECT * FROM clients WHERE username =%s", (username,)):
                flash("the username is already exists")
            else:
                sql = f"INSERT INTO clients (email, username, password, state) VALUES ('{email}', '{username}', '{password}', '{state}')"

                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for('login'))

    return render_template('signup.html')
