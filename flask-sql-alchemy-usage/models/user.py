'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
from database.config import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    address  = db.relationship('AddressModel',backref='user',uselist=False,lazy=True)

    def __init__(self,username,password):
        self.username = username
        self.password = password
    def json(self):
        return {"id":self.id,"username":self.username,"password":self.password,"address":self.address.json()}
    
    @classmethod  
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first().json()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self.id
      
      
      
        