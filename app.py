from flask import Flask
from flask_mysqldb import MySQL
import Haltura.routes

app = Flask(__name__, template_folder="./templates")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Haltura'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

