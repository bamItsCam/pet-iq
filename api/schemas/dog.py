#!/usr/bin/env python3
from marshmallow import Schema, fields
from api.schemas.score import ScoreSchema

class DogSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    breed = fields.String(required=True)
    owner = fields.String(required=True)
    scores = fields.Nested(ScoreSchema, required=False, many=True)
