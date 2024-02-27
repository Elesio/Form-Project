from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import send_file
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import os
from io import StringIO, BytesIO
import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="natlanmap39", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    isadmin VARCHAR(255)
);
""")

tid = 5
tname = 'FabulousFox'
tpass = 'xx_superduperpasswordextreme_xx'
tadmin = 'maybe'

cur.execute("""INSERT INTO users (id, username, password, isadmin) VALUES
(1, 'Elesio', 'goodpassword', 'y'),
(2, 'Nadoriana', 'vergoodpassword', 'y'),
(3, 'Supefredi', 'passwordmanager', 'y'),
(4, 'Antiunkraut', 'password', 'n');
""")

sql = cur.mogrify("""INSERT INTO users (id, username, password, isadmin) VALUES (%s, %s, %s, %s);""", (tid,tname,tpass,tadmin))
cur.execute(sql)

cur.execute("""SELECT * FROM users""")

print(cur.fetchall())

conn.commit()

cur.close()
conn.close()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databank.db'
app.config['SECRET_KEY'] = '71EU8gnZqZQ'
db = SQLAlchemy(app)

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

with app.app_context():
    db.create_all()

@app.route("/adduser")
def adduser():
    return render_template("adduser.html")

@app.route("/conf",methods=['POST'])
def pagestart():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return 'Hast du doch eingeloggt?'
    
@app.route("/list",methods=['GET','POST'])
def list():
    return render_template('list.html')

@app.route("/files",methods=['POST'])
def files():
    if request.method == 'POST':
        file = request.files['file']

        upload = Upload(filename=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()

        return f'Uploaded: {file.filename}'
    
@app.route('/d',methods=['POST'])
def download():
    start = 0
    end = 0
    for i in range(100):
        try:
            upload = Upload.query.filter_by(id=i).first()
            f = BytesIO(upload.data)
            start = start + 1
        except:
            upload = Upload.query.filter_by(id=i).first()
            end = end + 1
    
    filepath = app.root_path + '\myfile.txt'
    upload = Upload.query.filter_by(id=start).first()
    bytedata = BytesIO(upload.data)

    b = bytedata.read()
    
    with open(filepath, 'a') as fo:
        fo.write("%sstart is " % start)
        fo.write("%s and end is " % end)
        fo.write(str(type(bytedata)))
    
    return send_file(BytesIO(upload.data), download_name=upload.filename, as_attachment=True)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/form",methods=['POST'])
def form():
    return render_template('new.html')

@app.route("/py")
def loginnow():
    return render_template('form.html')

@app.route("/<string:filename>")
def givefile(filename):
    return send_file(filename)

@app.route("/fileinp",methods=['POST'])
def fileinp():
    usefile = app.root_path + '\myfile.txt'
    with open(usefile, 'r') as fo:
        content = fo.readlines()
    #hier muss der File eingelesen werden
        fulllist = []
    for item in content:
        newlist = item.split(',')
        newnewlist = []
        for entry in newlist:
            new = entry.replace('\n','')
            newnewlist.append(new)
        newnewlist.append('endline')
        fulllist.append(newnewlist)
    thinglist = []
    for thing in fulllist:
        for thing2 in thing:
            thinglist.append(thing2)
    return thinglist

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