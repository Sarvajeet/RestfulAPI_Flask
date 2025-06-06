# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:19:59 2019

@author: Sarva
"""

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# User data stored in a dictionary for efficient O(1) lookups by name.
# Previously, this was a list, requiring O(n) iteration.
users_dict = {
    "Nicholas": {"age": 42, "occupation": "Network Engineer"},
    "Elvin": {"age": 32, "occupation": "Doctor"},
    "Jass": {"age": 22, "occupation": "Web Developer"}
}

class User(Resource):
    
    def get(self,name):
        # Direct dictionary access for user lookup (O(1) average time complexity).
        if name in users_dict:
            user_data = users_dict[name]
            # Reconstruct the response to include the name, matching original behavior
            return {"name": name, "age": user_data["age"], "occupation": user_data["occupation"]}, 200
        return "User not found", 404


api.add_resource(User, "/user/<string:name>")
# Run the Flask app. Debug mode is set to False for production readiness (security/performance).
app.run(port='5003',debug=False)