'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
import _functools

from flask import make_response
from functools import wraps
from flask.globals import request

def validate_user(username,password):
    return True
  
def authenticate(func):
    @wraps(func)
    def any_name(*args,**kwargs):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            resp = make_response("Missing user information",400)
            resp.headers["WWW-Authenticate"]= 'Basic realm="Login Required"'
            return resp
        elif not validate_user(auth.username, auth.password):
            resp = make_response("Invalid credentials",401)
            resp.headers["WWW-Authenticate"]= 'Basic realm="Login Required"'
            return resp
        return func(*args,**kwargs)
    return any_name