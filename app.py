from flask import Flask, render_template
# from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Haltura!"
