from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    name = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)

    animals = db.relationship('Animal', back_populates='zookeeper')

class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    name = db.Column(db.String)

    id = db.Column(db.Integer, primary_key=True)

    animal = db.relationship('Animal', back_populates='enclosure')

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    zookeeper = db.relationship('Zookeeper', back_populates="animals")
    enclosure = db.relationship('Enclosure', back_populates='animal')

