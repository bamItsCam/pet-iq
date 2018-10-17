from api import db

class Owner(db.Model):
	__tablename__ = 'owners'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	firstname = db.Column(db.String(128))
	lastname = db.Column(db.String(128))
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	city = db.Column(db.String(128))
	state = db.Column(db.String(128))
	zip_code = db.Column(db.String(5))
	password_hash = db.Column(db.String(128))
	dogs = db.relationship('Dog', backref='owners', lazy='dynamic')

	def __repr__(self):
		return '<Owner {}>'.format(self.username)