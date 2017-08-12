'''
Created on 11 Aug 2017

@author: neeraj.mahajan
'''



from org.mahajan.entities.datamodel import Customer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from org.mahajan.entities.datamodel import  Base


class CustomerService(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        engine = create_engine('sqlite:///:memory:', echo=True)

        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
        self.session = Session()
    
    def addCustomer(self,customer):
        self.session.add(customer)
        self.session.commit()
        customer = self.session.query(Customer).filter_by(name=customer.name).first()
        return customer.id
    
    def getCustomer(self,customerId):
        customer = self.session.query(Customer).filter_by(id=customerId).first()
        print ("customer##################", customer)
        return customer

