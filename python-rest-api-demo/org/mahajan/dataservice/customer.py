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

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
                
        self.session = Session()
    
    def addCustomer(self,customer):
        print ("session value" , self.session)
        self.session.add(customer)
        self.session.commit()
    
    def getCustomer(self,customerId):
        print ("Hi I am called with customerId" , customerId)
        customer = self.session.query(Customer).filter_by(id=customerId) 
        print ("customer##################")
        return customer
