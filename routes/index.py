from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template ('home.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

