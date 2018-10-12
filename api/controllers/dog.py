#!/usr/bin/env python3

# processes data from the model and hands it to the router.
# Heavy logic/lifting should be done here or by helpers of controllers (e.g. engines)

from api import db
from api.models.dog import Dog
from api.models.owner import Owner
from api.schemas.dog import DogSchema
from marshmallow import ValidationError
from api.common.http import BadRequest, OkRequest

class DogController():
	def getList():
		return OkRequest(DogSchema(many=True).dump(Dog.query.all()))

	def getDogs(ownerId):
		return okRequest(DogSchema(many=True).dump(Dog.query.filter(Dog.owner.id == ownerId)))

	def getDog(id):
		return OkRequest(DogSchema().dump(Dog.query.get(id)))

	def create(respJson):
		try:
			valid = DogSchema().load(respJson)
		except ValidationError as e:
			return BadRequest(e.messages)
		else:
			# Make sure the owner is actually real...
			o = Owner.query.get(valid['owner'])
			if o:
				d = Dog(name=valid['name'], owner=valid['id'], breed=valid['breed'])
				db.session.add(d)
				db.session.commit()
				return OkRequest(DogSchema().dump(d))
			return BadRequest("Owner not found")

	def delete(id):
		d = Dog.query.get(id)
		db.session.delete(d)
		db.session.commit()
		return OkRequest("Deleted")
