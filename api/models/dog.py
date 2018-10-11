from api import db

class Dog(db.Model):
	__tablename__ = 'dogs'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	age = db.Column(db.Integer)
	breed = db.Column(db.String(128))
	owner = db.Column(db.Integer, db.ForeignKey('owners.id'))
	scores = db.relationship('Score', backref='dogs', lazy='dynamic')

	def __repr__(self):
		return '<Dog {}/{}>'.format(self.owner.username,self.name)
