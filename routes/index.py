from app import app, mysql
from flask import render_template, request, redirect, url_for


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_type = request.form['user-type']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        state = request.form['state']
        full_name = request.form['full-name']
        about_yourself = request.form['about-yourself']
        occupation = request.form.get('occupation', None)
        experience = request.form.get('experience', None)
        conn = mysql.connection
        cursor = conn.cursor()

        if user_type == 'client':
            sql = f"INSERT INTO users(email,username) VALUES('{email}','{ username}')"
        else:
            sql = f"INSERT INTO users(email,username) VALUES('{email}','{username}')"

        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return "User registered successfully!"  # Move this line outside the 'else' block

        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/home')

    return render_template('signup.html')