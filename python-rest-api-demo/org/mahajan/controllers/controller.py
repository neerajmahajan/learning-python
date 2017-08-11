'''
Created on 10 Aug 2017

@author: neeraj.mahajan
'''

from flask.globals import request
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
        
        self.customerDataService.addCustomer(customer)
    
    def getCustomer(self,customerId):
        return self.customerDataService.getCustomer(customerId)
    