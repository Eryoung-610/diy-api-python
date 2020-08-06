from api import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Chonk(db.Model):
    __tablename__='chonks'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable = False)
    species = db.Column(db.String, nullable = False)
    weight = db.Column(db.Integer)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'weight': self.weight
        }

    def __repr__(self):
        return f'Chonk \nid: {self.id}\nname:{self.name}\nspecies:{self.species}\nweight:{self.weight}'