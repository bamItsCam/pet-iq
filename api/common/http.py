#!/usr/bin/env python3
from flask import Response as R
import json

class Response(R):
    default_mimetype = "application/json"


# Two approaches here: Either have a lookup table of codes, or
class StatusCodes():
    Ok = 200
    BadRequest = 400


# have classes for each status code type. allows you to template responses

class BadRequest(Response):
    def __init__(self, error, **kwargs):
        s=401
        d = {'statusCode': s,
             'badRequest': error}
        r = json.dumps(d)
        super(BadRequest, self).__init__(response=r, status=s, **kwargs)

class OkRequest(Response):
    def __init__(self, content, **kwargs):
        s=200
        d = {'statusCode': s,
             'content': content}
        r = json.dumps(d)
        super(OkRequest, self).__init__(response=r, status=s, **kwargs)