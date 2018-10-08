#!/usr/bin/env python3

from flask import Flask
from flask import request
from api import app
from api.controllers.owner import OwnerController as controller
import json

v1Root = "/api/v1/"

# the heart of the api, handles routing and calls controllers

@app.route('/')
def hello():
	return "Hi"

@app.route(v1Root + "owner", methods=['GET', 'POST'])
def owner():
	if request.method == 'GET':
		return json.dumps([o.__dict__ for o in controller.getList()])
	else:
		username = request.args.get('username')
		email = request.args.get('email')
		password = request.args.get('password')
		return json.dumps(controller.create(username,email,password).__dict__)

@app.route(v1Root + "owner/<id>", methods=['GET','DELETE'])
def ownerId(id):
	if request.method == 'GET':
		return json.dumps(controller.getOwner(id).__dict__)
	else:
		return json.dumps(controller.delete(id).__dict__)