from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask_login import UserMixin
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/postgres'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='students'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(80),nullable=False)

    def __init__(self,username,password):
        self.username=username
        self.password=password

@app.route("/conf")
def pagestart():
    return render_template('index.html')

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/py")
def loginnow():
    return render_template('form.html')

@app.route('/login',methods=['GET','POST'])
def pyserv():
    name = 'Zin'
    if request.method == 'POST':
        name = request.form['name']
        return 'Hello ' + name + '!'
    else:
        print('get')
        name = request.args.get('name')
        return 'Tschüss ' + name + '!'

if __name__ == "__main__":
    app.run(debug=True)

@app.context_processor
def example():
    return dict(myexample='this is an example')