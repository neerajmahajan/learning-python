'''
Created on 10 Aug 2017

@author: neeraj.mahajan
'''

class Customer1 (object):
    '''
    classdocs
    '''
    __id=None
    __firstName=None
    __lastName=None
    __dob=None


    def __init__(self, id,firstName,lastName,dob):
        '''
        Constructor
        '''
        self.__id=id
        self.__firstName=firstName
        self.__lastName=lastName
        self.__dob=dob
    
    @property
    def id(self):
        return self.id
    
    @id.setter
    def id(self,value):
        self.__id = value
    
    @property
    def firstName(self):
        return self.__firstName
    
    @firstName.setter
    def firstName(self,value):
        self.__firstName = value
    
    @property
    def lastName(self):
        return self.__lastName
    
    @lastName.setter
    def lastName(self,value):
        self.__lastName = value
    
    @property
    def dob(self):
        return self.__dob
    
    @dob.setter
    def dob(self,value):
        self.__dob = value
    
    def serialize(self):
        return {
            "id":self.id,
            "firstName":self.firstName,
            "lastName": self.lastName,
            "dob":self.dob
            } 