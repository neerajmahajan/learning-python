'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
from database.config import db
from test import test_ipaddress


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    address  = db.relationship('AddressModel',backref='user',lazy=True)
    #backref is a simple way to also declare a new property 'user' on the AddressModel class. 

    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def add_address(self,address):
        self.address.append(address)
        
    def json(self):
        return {"id":self.id,"username":self.username,"password":self.password,"addresses":[addr.json() for addr in self.address ]}
    
    @classmethod  
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first().json()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self.id
      
      
      
        