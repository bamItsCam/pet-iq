#!/usr/bin/env python3

class OwnerRequests():
    def __init__(self, **dict):
        # self.__dict__ = dict
        # or
        # is it better to explicitly say what members there are?
        self.username = dict['username']
        self.email = dict['email']
        self.password = dict['password']

#