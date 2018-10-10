#!/usr/bin/env python3

class DogRequests():
    def __init__(self, **dict):
        self.name = dict['name']
        self.owner = dict['owner']
        self.breed = dict['breed']

#