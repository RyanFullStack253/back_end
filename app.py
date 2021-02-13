# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:37:28 2020

@author: RYAN EDEM KPODO
"""
from flask import Flask, jsonify, request,\
    Response
from Model import User, Contact, Register
from settings import *
import json
import jwt, datetime
from functools import wraps
from flask_cors import CORS
 
CORS(app)

# User Table 

@app.route('/add/user', methods=["POST"])
def add_user():
    request_data = request.get_json()
    User.addUser(request_data['username'], request_data['password'])
    response = Response("", 200, mimetype='application/json')
    return response
    
@app.route('/get/users')
def get_all_users():
    return jsonify({"users": User.getAllUsers()})
        
# Contact Table 
        
@app.route('/add/contact', methods=["POST"])
def add_contact():
    request_data = request.get_json()
    Contact.addContact(request_data['name'], request_data['phone_number'], request_data['email'], request_data['preference'], \
                       request_data['message'])
    requestData = {
            "message": "success",
            "status": 200,
            "data": request_data
    }
    response = Response(json.dumps(requestData), 200, mimetype='application/json')
    return response

@app.route('/get/contacts')
def get_all_contacts():
    return jsonify({"contacts": Contact.getAllContacts()})
        
# Register Table 

@app.route('/add/register', methods=["POST"])
def add_register():
    request_data = request.get_json()
    Register.addRegister(request_data['first_name'], request_data['last_name'], request_data['other_name'], request_data['email'], \
                         request_data['password'])
    requestData = {
            "message": "success",
            "status": 200,
            "data": request_data
        }
    response = Response(json.dumps(requestData), 200, mimetype='application/json')
    return response

@app.route('/get/registers')
def get_all_registers():
    return jsonify({"registers": Register.getAllRegisters()})

if __name__ == "__main__":
    app.run() 