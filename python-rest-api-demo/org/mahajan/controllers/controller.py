'''
Created on 10 Aug 2017

@author: neeraj.mahajan
'''

import json

from flask import jsonify
from flask.globals import request
from flask.helpers import url_for
from flask_restful import  Resource

from org.mahajan.dataservice.customer import CustomerService
from org.mahajan.entities.datamodel import Customer


class CustomerController(Resource):
    '''
    Hi I am a customer controller
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.customerDataService = CustomerService()
         
    def addCustomer(self):
        name = request.form["name"];
        fullname = request.form["fullname"];
        password = request.form["password"];
        
        customer = Customer(name=name, fullname=fullname, password=password)
        
        customerId = self.customerDataService.addCustomer(customer)
        return jsonify ({
            
            "id": customerId,
            "url": url_for("getCustomer",customerId=customerId)
            
            })
    
    def getCustomer(self,customerId):
        customer = self.customerDataService.getCustomer(customerId)
        return jsonify(customer.serialize())
    