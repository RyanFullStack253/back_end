# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 18:43:34 2020

@author: RYAN EDEM KPODO
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import app
from datetime import datetime
from flask_script import Manager 
from flask_migrate import Migrate, \
    MigrateCommand
import json

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', Manager)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key\
                   =True, autoincrement=\
                       True)
    username = db.Column(db.String(80), \
                         nullable=False)
    password = db.Column(db.String(80), \
                          nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    def json_1(self):
        return {
                "id": self.id,
                "username": self.username,
                "password": self.password
            }
    def __repr__(self):
        return json.dumps({
                "id": self.id,
                "username": self.username,
                "password": self.password
                }
                )
    def addUser(_username, _password):
        new_user = User(username=_username\
                        , password=\
                            _password)
        db.session.add(new_user)
        db.session.commit()
    def getAllUsers():
        return [User.json_1(user) for user\
                in User.query.all() ]
            
class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    preference = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(250), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def json_1(self):
        return{
                "id": self.id,
                "name": self.name,
                "phone_number": self.phone_number,
                "email": self.email,
                "preference": self.preference,
                "message": self.message
            }
    def __repr__(self):
        return json.dumps({
                "id": self.id,
                "name": self.name,
                "phone_number": self.phone_number,
                "email": self.email,
                "preference": self.preference,
                "message": self.message
            })
    def addContact(_name, _phone_number, _email, _preference, _message):
        new_contact = Contact(name=_name, phone_number=_phone_number, email=_email,\
                              preference=_preference, message=_message)
        db.session.add(new_contact)
        db.session.commit()
    def getAllContacts():
        return[Contact.json_1(contact) for contact in Contact.query.all()]
    
class Register(db.Model):
     __tablename__ = "registers"
     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     first_name = db.Column(db.String(50), nullable=False)
     last_name = db.Column(db.String(50), nullable=False)
     other_name = db.Column(db.String(50), nullable=True)
     email = db.Column(db.String(80), nullable=False)
     password = db.Column(db.String(50), nullable=False)
     created_on = db.Column(db.DateTime(), default=datetime.utcnow)
     updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
     
     def json_1(self):
         return{
                 "id": self.id,
                 "first_name": self.first_name,
                 "last_name": self.last_name,
                 "other_name": self.other_name,
                 "email": self.email,
                 "password": self.password
             }
     def __repr__(self):
         return json.dumps({
                 "id": self.id,
                 "first_name": self.first_name,
                 "last_name": self.last_name,
                 "other_name": self.other_name,
                 "email": self.email,
                 "password": self.password
             })
     def addRegister(_first_name, _last_name, _other_name, _email, _password):
         new_register = Register(first_name=_first_name, last_name=_last_name,\
                                 other_name=_other_name, email=_email, password=_password)
         db.session.add(new_register)
         db.session.commit()
     def getAllRegisters():
        return[Register.json_1(register) for register in  Register.query.all()]