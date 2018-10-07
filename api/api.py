#!/usr/bin/env python3

from flask import Flask
from flask import request
from controllers.owner import controller
app = Flask(__name__)

v1Root = "/api/v1/"

# the heart of the api, handles routing and calls controllers

@app.route('/')
def hello():
	return "Hi"

@app.route(v1Root + "owner", methods=['GET', 'POST'])
def owner():
	if request.method == 'GET':
		return controller.getList()
	else:
		return controller.create(request.form['username'])

@app.route(v1Root + "owner/<id>", methods=['GET'])
def ownerId(id):
	if request.method == 'GET':
		return controller.getUser(id)

if __name__ == '__main__':
	app.run()