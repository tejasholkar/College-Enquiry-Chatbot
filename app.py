from chatbot import chatbot
import flask  # explicit flask namespace import
from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from flask_recaptcha import ReCaptcha
import flask_recaptcha
from markupsafe import Markup
import os
try:
    import mysql.connector  # mysql connector import, will be None if not installed
    MYSQL_AVAILABLE = True
except ImportError:
    MYSQL_AVAILABLE = False
import sqlite3

# Compatibility patch: older flask_recaptcha versions expect Markup in module globals.
flask_recaptcha.Markup = Markup

app = Flask(__name__)
recaptcha = ReCaptcha(app=app)
app.secret_key=os.urandom(24)
app.static_folder = 'static'


app.config.update(dict(
    # Disable ReCaptcha by default for local development. Set to True in production if keys are valid.
    RECAPTCHA_ENABLED = False,
    RECAPTCHA_SITE_KEY = "6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L",
    RECAPTCHA_SECRET_KEY = "6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee"
))

recaptcha=ReCaptcha()
recaptcha.init_app(app)

app.config['SECRET_KEY'] = 'cairocoders-ednalan'

def ensure_sqlite_schema():
    """Create required fallback tables when running on SQLite."""
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS suggestion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)
    conn.commit()

# database connectivity: try MySQL, fallback to SQLite if MySQL not available or unreachable
conn = None
cur = None
if MYSQL_AVAILABLE:
    try:
        conn = mysql.connector.connect(host='localhost',port='3306',user='root',password='candida1',database='register')
        cur = conn.cursor()
        print("Connected to MySQL database 'register'")
    except Exception as e:
        print("MySQL connection failed, falling back to SQLite. Error:\n", e)

if not cur:
    # Use sqlite3 as a fallback for local development (file: database.sqlite3)
    conn = sqlite3.connect('database.sqlite3', check_same_thread=False)
    cur = conn.cursor()
    ensure_sqlite_schema()
    print("Using SQLite database 'database.sqlite3' (fallback)")

# Google recaptcha - site key : 6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L
# Google recaptcha - secret key : 6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee

@app.route("/index")
def home():
    if 'id' in session:
        return render_template('index.html')
    else:
        return redirect('/')


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cur.fetchall()
    if len(users)>0:
        session['id']=users[0][0]
        flash('You were successfully logged in')
        return redirect('/index')
    else:
        flash('Invalid credentials !!!')
        return redirect('/')
    # return "The Email is {} and the Password is {}".format(email,password)
    # return render_template('register.html')

@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('name') 
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    #cur.execute("UPDATE users SET password='{}'WHERE name = '{}'".format(password, name))
    cur.execute("""INSERT INTO  users(name,email,password) VALUES('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser=cur.fetchall()
    flash('You have successfully registered!')
    session['id']=myuser[0][0]
    return redirect('/index')

@app.route('/suggestion',methods=['POST'])
def suggestion():
    email=request.form.get('uemail')
    suggesMess=request.form.get('message')

    cur.execute("""INSERT INTO  suggestion(email,message) VALUES('{}','{}')""".format(email,suggesMess))
    conn.commit()
    flash('You suggestion is succesfully sent!')
    return redirect('/index')

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')  
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    # app.secret_key=""
    app.run() 
print("Hello world")
