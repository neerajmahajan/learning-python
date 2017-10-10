'''
Created on 10 Oct 2017

@author: neeraj.mahajan
'''
from database.config import db
from test import test_namespace_pkgs


student_course = db.Table('student_course',
                          db.Column('student_id',db.Integer,db.ForeignKey('student.student_id'),primary_key=True),
                          db.Column('course_id',db.Integer,db.ForeignKey('course.course_id'),primary_key=True),
                          )

class StudentModel(db.Model):
    __tablename__ = 'student'
    student_id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender  = db.Column(db.String(100))
    
    courses = db.relationship('CourseModel',secondary=student_course,lazy='subquery', backref=db.backref('students',lazy=True))
    
    def __init__(self,name,age,gender):
        self.name = name
        self.age  = age
        self.gender = gender
        self.course_names = []
    
    def assign_course(self,course_name):
        self.course_names.append(course_name)
        
    def json(self):
        return {"student_id":self.student_id,"name":self.name,"age":self.age,"gender":self.gender,"courses":[course.json() for course in self.courses]}
   
    @classmethod
    def find_by_student_id(cls,id):
        return cls.query.filter_by(student_id=id).first()
      
    def save_to_db(self):
        for course_name in self.course_names:
            self.courses.append(CourseModel.find_by_course_name(course_name))
        db.session.add(self)
        db.session.commit()
        return self.student_id


class CourseModel(db.Model):
    __tablename__ = 'course'

    course_id  = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100))
    
    def __init__(self,course_name):
        self.course_name = course_name
        
    def json(self):
        return {"course_id":self.course_id,"course_name":self.course_name}
   
    @classmethod
    def find_by_course_name(cls,name):
        return cls.query.filter_by(course_name=name).first()
      
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self.course_id