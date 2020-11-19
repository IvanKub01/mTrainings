from train import db, ma
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


class zoznam(db.Model):
    __tablename__ = 'zoznam'
    idcko = db.Column(db.Integer, primary_key=True,autoincrement = True)
    nick = db.Column(db.Unicode(250),nullable=False)
    password = db.Column(db.Unicode(250),nullable=False)

    def __repr__(self):
        return self.Name

#marshmallow - SQLalchemy objekt konverzia to JSON
class zoznamSchema(ModelSchema):
    class Meta:
        model = zoznam



