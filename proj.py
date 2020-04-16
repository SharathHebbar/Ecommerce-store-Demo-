from flask import *
from flask_mysqldb import MySQL, MySQLdb


app = Flask(__name__)
app.secret_key = "flask"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'campus-plexus'
mysql = MySQL(app)

#home
@app.route('/')
def home():
    return redirect(url_for('signup'))

#signup
@app.route('/signup/')
def signup():
    return render_template('index.html')

#Collision
@app.route('/collision/')
def collision():
    return render_template('demo.html')