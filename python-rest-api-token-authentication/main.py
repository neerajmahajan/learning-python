'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''

from flask.app import Flask
from flask_restful import Api
from flask_jwt import JWT,jwt_required
from security import validate_user,get_user_based_on_identity
from resource import MyHanlder


def main():
    '''
    This method registers all the end points of the application
    '''
    app = Flask(__name__)
    app.secret_key = 'some_secret_key'
    api = Api(app)
    jwt = JWT(app,validate_user,get_user_based_on_identity)
    api.add_resource(MyHanlder, '/api/hello')
    return app
  
def run_main():
    main().run(debug=False)


if __name__ == '__main__':
    run_main()