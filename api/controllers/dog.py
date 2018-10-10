#!/usr/bin/env python3

# processes data from the dto and hands it to the router.
# Heavy logic/lifting should be done here or by helpers of controllers (e.g. engines)

from api import db
from api.models.dog import Dog
from api.models.owner import Owner
from api.dto.dog import DogDTO
from api.requests.dog import DogRequests

class DogController():
	def getList():
		return [DogDTO(d) for d in Dog.query.all()]

	def getDogs(ownerId):
		return [DogDTO(d) for d in Dog.query.filter(Dog.owner.id == ownerId)]

	def getDog(id):
		return DogDTO(Dog.query.get(id))

	def create(r: DogRequests):
		# Make sure the owner is actually real...
		o = Owner.query.get(r.owner)		
		if o is not None:
			d = Dog(name=r.name, owner=o.id, breed = r.breed)
			db.session.add(d)
			db.session.commit()
			return DogDTO(d)
		return None

	def delete(id):
		d = Dog.query.get(id)
		db.session.delete(d)
		db.session.commit()
		return DogDTO(d)
