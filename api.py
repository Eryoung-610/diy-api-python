from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pentaxs5i@localhost/flaskAPI_hw'

from chonk_crud import *

@app.route('/')
def home():
    return jsonify({'message' : 'This works'})

@app.route('/chonks', methods=['GET','POST'])
def all_chonks():
    if request.method == 'GET':
        return get_all_chonks()
    if request.method =='POST':
        create_chonk(request.form['name'], request.form['species'], request.form['weight'])
        return redirect('/chonks')

@app.route('/chonk/<id>', methods = ['GET','PUT', 'DELETE'])
def chonk_detail(id):
    if request.method == 'GET':
        return get_chonk(id)
    if request.method == 'PUT':
        return update_chonk(id, request.form['name'], request.form['species'], request.form['weight'])
    if request.method == 'DELETE':
        return destroy_chonk(id)