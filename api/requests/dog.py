#!/usr/bin/env python3
from flask_restful import Resource, Api, reqparse

api = Api(app)

class DogRequest():
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=string,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('breed',
                        type=string,
                        required=True,
                        help="This field cannot be left blank"
                        )

    def post(self, name):
        data = DogRequests.parser.parse_args()
        dog_data = {"name": data['name'], "breed", data['breed']}
        return dog_data, 201

api.add_resource(DogCreation, '/dog')