from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder="Haltura/templates")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Kfir2208'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)


@app.route('/')
def index():
    return "Welcome to Haltura!"
