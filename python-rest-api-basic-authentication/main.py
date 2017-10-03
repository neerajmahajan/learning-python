'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''

from flask.app import Flask
from flask_restful import Api

from resource import MyHanlder


def main():
    '''
    This method registers all the end points of the application
    '''
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(MyHanlder, '/api/hello')
    return app
  
def run_main():
    main().run(debug=False)


if __name__ == '__main__':
    run_main()