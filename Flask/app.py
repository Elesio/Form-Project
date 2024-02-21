from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import send_file
import shutil
'''from flask_login import UserMixin
import psycopg2'''
import os

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

@app.route("/<string:filename>")
def givefile(filename):
    return send_file(filename)

@app.route('/login',methods=['GET','POST'])
def pyserv():
    name = 'Zin'
    if request.method == 'POST':
        newsave = []
        #hier rein: Die Werteumwandeln in eine Datei
        filepath = app.root_path + '\myfile.txt'
        if os.path.exists(filepath):
            os.remove(filepath)
        with open(filepath, 'a') as fo:
            #fo.write("This is Test Data")
            for item in request.json:
                newlist = []
                if len(item)!=len(request.json[0]):
                    for thing in item:
                        newlist.append(thing)
                    for l in range(len(request.json[0])-len(item)):
                        newlist.append('')
                else:
                    for thing in item:
                        newlist.append(thing)
                newsave.append(newlist)
            for i in range(len(newsave)):
                for ii in range(len(newsave[0])):
                    if ii != len(newsave[0])-1 and newsave[i][ii+1]!='':
                        fo.write("%s," % newsave[i][ii])
                    elif ii == len(newsave[0])-1 or newsave[i][ii+1]=='':
                        fo.write("%s" % newsave[i][ii])
                        fo.write('\n')
            fo.close()
        #return request.json
            return filepath
    else:
        print('get')
        name = 'Noah'
        return 'Tschüss ' + name + '!'

if __name__ == "__main__":
    app.run(debug=True)

@app.context_processor
def example():
    return dict(myexample='this is an example')