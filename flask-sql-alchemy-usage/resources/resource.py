'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
from flask.globals import request
from flask_restful import Resource

from models.address import AddressModel
from models.user import UserModel
from models.college import CourseModel, StudentModel


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
        new_user = UserModel(username=username,password=password)
        address1 = AddressModel(county="Cornwall",user_id=None)
        address2 = AddressModel(county="Hampshire",user_id=None)
        new_user.add_address(address1)
        new_user.add_address(address2)
        return {"user_id": new_user.save_to_db()}
      
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

class CourseHandler(Resource):
    '''
    classdocs
    '''
    def get(self,name):
        return CourseModel.find_by_course_name(name).json()
      
    def post(self):
        request_data = request.get_json()
        course_name = request_data["course_name"]
        course = CourseModel(course_name)
        return {"course_id": course.save_to_db()}

class StudentHandler(Resource):
    '''
    classdocs
    '''
    def get(self,id):
        return StudentModel.find_by_student_id(id).json()
      
    def post(self):
        request_data = request.get_json()
        
        name = request_data["name"]
        age = request_data["age"]
        gender = request_data["gender"]
        
        student = StudentModel(name,age,gender)
        
        for course_name in request_data["courses"]:
            student.assign_course(course_name)
            
        return {"student_id": student.save_to_db()}
      