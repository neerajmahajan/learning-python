'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''

from flask.app import Flask
from flask_restful import Api

from resources.resource import UserHandler, AddressHandler, CourseHandler, StudentHandler


def main():
    '''
    This method registers all the end points of the application
    '''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app)
    
    @app.before_first_request
    def create_tables():
      db.create_all()
      
    api.add_resource(UserHandler, '/api/user','/api/user/<string:name>')
    api.add_resource(AddressHandler, '/api/address','/api/address/<string:id>')
    api.add_resource(CourseHandler, '/api/course','/api/course/<string:name>')
    api.add_resource(StudentHandler, '/api/student','/api/student/<string:id>')

    from database.config import db
    db.init_app(app)
    app.run(debug=False)
  
if __name__ == '__main__':
      main()