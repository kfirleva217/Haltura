from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from flask_mysqldb import MySQL
from flask_migrate import Migrate

app = Flask(__name__, template_folder="./templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haltura.db'  # SQLite URI
app.secret_key = 'haltura'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
with app.app_context():
    # Create the database tables
    db.create_all()






from routes import index
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'admin'
# app.config['MYSQL_DB'] = 'Haltura'
# mysql = MySQL(app)

