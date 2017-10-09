'''
Created on 9 Oct 2017

@author: neeraj.mahajan
'''
from database.config import db


class AddressModel(db.Model):
      __tablename__ = 'address'
      id = db.Column(db.Integer, primary_key=True)
      county = db.Column(db.String(100))
      user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)

      def __init__(self, county,user_id):
        self.county = county
        self.user_id = user_id
      
      def json(self):
        return {"id":self.id,"county":self.county,"user_id":self.user_id}
        
      @classmethod  
      def find_by_id(cls,id):
          address = cls.query.filter_by(id=id).first()
          print (address.user.json())
          return address.json()
      
      def save_to_db(self):
          db.session.add(self)
          db.session.commit()
          return self.id