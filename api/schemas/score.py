#!/usr/bin/env python3
from marshmallow import Schema, fields

class ScoreSchema(Schema):
    id = fields.Int(dump_only=True)
    timestamp = fields.Time(required=True)
    iq = fields.Int(required=True)
    dog = fields.Int(required=True)