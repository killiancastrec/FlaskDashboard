from flask import Flask, render_template, request, json, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
port = 3000
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'JobBoardFlask'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

