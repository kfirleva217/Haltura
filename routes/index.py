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
    f=open('/Users/kfir/log.txt','a')
    f.write("Welcome")
    f.close()
    if request.method == 'POST':
        f = open('/Users/kfir/log.txt', 'a')
        f.write("post")
        f.close()
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
            cursor.execute(
                "INSERT INTO users (email, username, password, user_type, state, full_name, about_yourself) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (email, username, password, user_type, state, full_name, about_yourself)
            )
        else:
            cursor.execute(
                "INSERT INTO users (email, username, password, user_type, occupation, experience, full_name, about_yourself) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (email, username, password, user_type, occupation, experience, full_name, about_yourself)
            )
            return "User registered successfully!"
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('success'))

    return render_template('signup.html')

