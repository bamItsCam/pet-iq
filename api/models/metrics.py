from api import db

class Metrics(db.Model):
    __tablename__ = 'metrics'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(128))
    subpath = db.Column(db.String(128))
    count = db.Column(db.Integer)

    def __repr__(self):
        return '<Metric {}/{}/{}'.format(self.subpath, self.method, self.count)