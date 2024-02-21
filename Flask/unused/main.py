from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:natlanmap39@localhost/students'

db=SQLAlchemy(app)
#https://www.youtube.com/watch?v=XZ_gAWdGzZk