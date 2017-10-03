'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
from flask import make_response
from functools import wraps
from flask.globals import request
from model import User
def validate_user(username,password):
    return User(1,"neeraj","test")
  
def get_user_based_on_identity(payload):
    user_id = payload['identity']
    #use this user_id and retrieve user from database based on this id
    return User(1,"neeraj","test")