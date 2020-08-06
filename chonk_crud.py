from models import Chonk, db
from flask import jsonify, redirect

def create_chonk(name,species,weight):
    weight = int(weight)
    chonk = Chonk(name=name, species=species,weight=weight)
    db.session.add(chonk)
    db.session.commit()
    return chonk

def get_all_chonks():
    all_chonks = Chonk.query.all()
    if all_chonks:
        all_chonks = [chonk.as_dict() for chonk in all_chonks]
        return jsonify(all_chonks)
        else: return jsonify({'message' : f'No Chonks in db'})

def get_chonk(id):
    chonk=Chonk.query.get(id)
    if chonk: return jsonify(chonk.as_dict())
    else: return jsonify({'message' : f'No Chonk found at id {id}'})

def update_chonk(id,name,species,weight):
    chonk = Chonk.query.get(id)
    if chonk:
        chonk.name = name or chonk.name
        chonk.species = species or chonk.species
        chonk.weight = weight or chonk.weight
        db.session.commit()
        return jsonify(chonk.as_dict())
    else: return jsonify({'message' : f'No chonk found at id {id}'})

def destroy_chonk(id):
    chonk = Chonk.query.get(id)
    if chonk:
        db.session.delete(chonk)
        db.session.commit()
        return redirect('/chonks')
    else: return jsonify({'message' : f'No chonk found at id {id}'})
