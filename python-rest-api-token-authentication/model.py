'''
Created on 3 Oct 2017

@author: neeraj.mahajan
'''
from test.support import _id

class User(object):
    '''
    classdocs
    '''


    def __init__(self, _id,username,password):
        self.id = _id
        self.username = username
        self.password = password