'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
from flask_restful import Resource

from security import authenticate


class MyHanlder(Resource):
    '''
    classdocs
    '''

    @authenticate
    def get(self):
        return "hello world"
        
        