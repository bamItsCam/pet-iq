#!/usr/bin/env python3

from api.models.owner import Owner
from api.dto.dog import DogDTO

class OwnerDTO():
	def __init__(self,owner: Owner):
		self.id = owner.id
		self.name  = " ".join([owner.firstname,owner.lastname])
		self.email = owner.email
		self.username = owner.username
		# The DTO should not ever reveal the owner's password hash!
		# DTO's should only contain lists of other DTO objects, NEVER models
		self.dogs = [DogDTO(d) for d in owner.dogs]