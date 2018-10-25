#!/usr/bin/env python3
from marshmallow import Schema, fields

class MetricSchema(Schema):
    id = fields.Int(dump_only=True)
    subpath = fields.String(required=True)
    method = fields.String(required=True)
    count = fields.Int(required=False)
