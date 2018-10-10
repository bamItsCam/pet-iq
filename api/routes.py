#!/usr/bin/env python3

from flask import Flask
from flask import request
from api import app
from api.controllers.owner import OwnerController as Owner
from api.requests.owner import OwnerRequests as ownerReq
from api.controllers.dog import DogController as Dog
from api.requests.dog import DogRequests as dogReq
import json

v1Root = "/api/v1/"

# the heart of the api, handles routing and calls controllers

@app.route('/')
def hello():
	return "Hi"

# Owner routes
@app.route(v1Root + "owner", methods=['GET', 'POST'])
def owner():
	if request.method == 'GET':
		return marshal(Owner.getList())
	else:
		return marshal(Owner.create(unmarshal(request, ownerReq)))

@app.route(v1Root + "owner/<id>", methods=['GET','DELETE'])
def ownerId(id):
	if request.method == 'GET':
		return marshal(Owner.getOwner(id))
	else:
		return marshal(Owner.delete(id))

# Dog routes		
@app.route(v1Root + "dogs/<ownerId>", methods=['GET'])
def ownerDogs():
	if request.method == 'GET':
		return marshal(Dog.getDogs())

@app.route(v1Root + "dog", methods=['GET', 'POST'])
def dog():
	if request.method == 'GET':
		return marshal(Dog.getList())
	else:
		return marshal(Dog.create(unmarshal(request, dogReq)))

@app.route(v1Root + "dog/<id>", methods=['GET','DELETE'])
def dogId(id):
	if request.method == 'GET':
		return marshal(Dog.getOwner(id))
	else:
		return marshal(Dog.delete(id))

#helpers (to be moved)

# convert json into object
def marshal(object):
	if type(object) is list:
		return json.dumps([o.__dict__ for o in object])
	else:
		return json.dumps(object.__dict__)


# convert request's body (json) into an object
def unmarshal(request, className):
	# unmarshaling the request body would be responsible for catching
	# key errors, aka
	print(request)
	print(className)
	dict = request.get_json()
	return className(**dict)
