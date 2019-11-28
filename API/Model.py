from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
ma = Marshmallow()
db = SQLAlchemy()


class Visitor(db.Model):
    __tablename__='visitor'
    id=db.Column(db.String(40),primary_key=True)
    phone_no=db.Column(db.String(10), nullable=False)
    name=db.Column(db.String(40), nullable=False)
    email=db.Column(db.String(85),nullable=False)
    timestamp=db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    checkintime=db.Column(db.DateTime,nullable=False)
    checkouttime=db.Column(db.DateTime,nullable=True)

    


    def __init__self(self,id,phone_no,name,email,checkintime):
        self.id=id
        self.phone_no=phone_no
        self.name=name
        self.email=email
        self.checkintime=checkintime


class Host(db.Model):
    __tablename__="host"
    id=db.Column(db.String(40),primary_key=True)
    phone_no=db.Column(db.String(10),nullable=False)
    name=db.Column(db.String(40), nullable=False)
    email=db.Column(db.String(85),nullable=False)


    def __init__self(self,id,phone_no,name,email):
        self.id=id
        self.phone_no=phone_no
        self.email=email
        self.name=name
