#!/usr/bin/env python3

# DTO - data transfer object. Takes data from db models and concats strips or formats the data. Useful when combining data from multiple tables.

from models.owner import model

class Owner():
	def get(self, id=None):
		if id:
			return str(model.get(int(id)))
		else:
			return ''.join(model.get(None))

	def create(self, username):
		return str(model.write(username))

dto = Owner()