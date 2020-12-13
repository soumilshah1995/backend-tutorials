try:
    from api.login.views import LoginController
    from api.controller.views import Controller

    from flask import Flask, request
    from flask_restful import Resource, Api, reqparse
except Exception as e:
    print("Error : {} ".format(e))

app = Flask(__name__)
api = Api(app)
