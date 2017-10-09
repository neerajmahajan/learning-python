'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
from flask.globals import request
from flask_restful import Resource

from models.address import AddressModel
from models.user import UserModel


class UserHandler(Resource):
    '''
    classdocs
    '''

    def get(self,name):
        return UserModel.find_by_username(name)
    def post(self):
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]
        user_id = UserModel(username=username,password=password).save_to_db()
        return {"user_id": user_id}
      
class AddressHandler(Resource):
    '''
    classdocs
    '''

    def get(self,id):
        return AddressModel.find_by_id(id)
    def post(self):
        request_data = request.get_json()
        county = request_data["county"]
        user_id = request_data["user_id"]
        address_id = AddressModel(county=county,user_id=user_id).save_to_db()
        return {"address_id": address_id}
      