'''
Created on 10 Aug 2017

@author: neeraj.mahajan
'''

from flask_restful import  Resource


class CustomerController(Resource):
    '''
    classdocs
    '''
    def test(self):
        return "Hello Customer"
    
    def test2(self,name):
        return "Hello " + name