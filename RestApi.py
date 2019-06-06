# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:19:59 2019

@author: Sarva
"""

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
    
    def get(self,name):
        for user in users:
            if (name==user["name"]):               
                return user, 200
        return "User not found", 404


api.add_resource(User, "/user/<string:name>")
app.run(port='5003',debug=True)