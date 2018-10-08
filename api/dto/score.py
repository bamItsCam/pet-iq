#!/usr/bin/env python3

from api.models.score import Score

class ScoreDTO():
	def __init__(self,score: Score):
		self.id = score.id
		self.timestamp  = score.timestamp
		self.iq = score.iq
		self.dog = score.dog.name