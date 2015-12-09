import os
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_UI'] = 'postgresql://localhost/testDB'
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello World!'
