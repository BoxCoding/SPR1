import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security.customer_validation import authentication_email,authentication_phone
from resource.user import CustomerRegistration

app=Flask(__name__)
api=Api(app)

jwt = JWT(app, authentication_email, authentication_phone)

api.add_resource(CustomerRegistration, '/signup')

if __name__ == '__main__':
    app.run(port=5050,debug=True)