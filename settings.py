# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 18:07:15 2020

@author: RYAN EDEM KPODO
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\RyanK\OneDrive\Desktop\python\database.db'
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']\
    = False