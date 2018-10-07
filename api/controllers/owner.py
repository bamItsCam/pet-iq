#!/usr/bin/env python3

# processes data from the dto and hands it to the router.
# Heavy logic/lifting should be done here or by helpers of controllers (e.g. engines)

from dto.owner import dto

class Owner():
	def getList(self):
		return dto.get()

	def getUser(self, id):
		return dto.get(id)

	def create(self, username):
		return dto.create(username)

controller = Owner()
