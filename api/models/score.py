from api import db
from datetime import datetime

class Score(db.Model):
	__tablename__ = 'scores'
	id = db.Column(db.Integer, primary_key=True)
	iq = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	dog = db.Column(db.Integer, db.ForeignKey('dogs.id'))

	def __repr__(self):
		return '<Score {}/{}/{}/{}>'.format(self.dog.owner.username,self.dog.name,self.timestamp,self.iq)