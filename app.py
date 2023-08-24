from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder="./templates")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password'
app.config['MYSQL_DB'] = 'Haltura'
mysql = MySQL(app)

from  routes import index