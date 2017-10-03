'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
from flask_restful import Resource

from flask_jwt import JWT,jwt_required

class MyHanlder(Resource):
    '''
    classdocs
    '''

    @jwt_required()
    def get(self):
        return "hello world"
        
        