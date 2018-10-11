#!/usr/bin/env python3

from api.models.dog import Dog
from api.dto.score import ScoreDTO

class DogDTO():
	def __init__(self,dog: Dog):
		self.id = dog.id
		self.name  = dog.name
		self.breed = dog.breed
		self.owner = dog.owner
		if dog.scores is not None and len(dog.scores.all()) > 0:
			self.current_score = ScoreDTO(max(dog.scores.all(), key=lambda item: item.timestamp))		
		else:
			self.current_score = 0
