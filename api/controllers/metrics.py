#!/usr/bin/env python3

from api import db
from api.models.metrics import Metrics
from api.common.http import OkRequest
from api.schemas.metrics import MetricSchema

class MetricController():
    def iterate(method, subpath):
        method = method.lower()
        cur = Metrics.query.filter_by(method=method, subpath=subpath).first()
        if cur:
            cur.count = cur.count + 1
            db.session.commit()
        else:
            new = Metrics(method=method, subpath=subpath, count=1)
            db.session.add(new)
            db.session.commit()

    def getAll():
        return OkRequest(MetricSchema(many=True).dump(Metrics.query.all()))