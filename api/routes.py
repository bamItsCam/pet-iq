#!/usr/bin/env python3

import json
from flask import Flask, request
from api import app
from api.controllers.owner import OwnerController as Owner
from api.controllers.dog import DogController as Dog
from api.controllers.metrics import MetricController as Metric

v1Root = "/api/v1"

# the heart of the api, handles routing and calls controllers

@app.route('/')
def hello():
	return "Hi"


# Owner routes
@app.route(v1Root + "/owners", methods=['GET', 'POST'])
def owner():
	if request.method == 'GET':
		print(request.path)
		return Owner.getList()
	else:
		return Owner.create(request.get_json())


@app.route(v1Root + "/owners/<id>", methods=['GET','DELETE'])
def ownerId(id):
	if request.method == 'GET':
		return Owner.getOwner(id)
	else:
		return Owner.delete(id)


# Dog routes		
@app.route(v1Root + "/dogs/<ownerId>", methods=['GET'])
def ownerDogs():
	if request.method == 'GET':
		return Dog.getDogs()


@app.route(v1Root + "/dogs", methods=['GET', 'POST'])
def dog():
	if request.method == 'GET':
		return Dog.getList()
	else:
		return Dog.create(request.get_json())


@app.route(v1Root + "/dogs/<id>", methods=['GET','DELETE'])
def dogId(id):
	if request.method == 'GET':
		return Dog.getOwner(id)
	else:
		return Dog.delete(id)


@app.route(v1Root + "/metrics", methods=['GET'])
def metrics():
	if request.method == 'GET':
		return Metric.getAll()


@app.before_request
def apiUsageMetrics():
	m = request.method
	p = request.path
	if "/owners" in p:
		Metric.iterate(subpath="/owners", method=m)
	elif "/dogs" in p:
		Metric.iterate(subpath="/dogs", method=m)
	elif "/metrics" in p:
		Metric.iterate(subpath="/metrics", method=m)
	else:
		Metric.iterate(subpath="unknown", method=m)
		# unknown ep requested