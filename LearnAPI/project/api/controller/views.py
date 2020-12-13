try:
    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse
    from flask_httpauth import HTTPBasicAuth
    import os
    import json
    import jwt
    import datetime
    import json
    from functools import wraps
except Exception as e:
    print("Error Loading libraries : {} ".format(e))

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = '8ee2923d3cd2b2833d3b747173f6c0da'


def verify_token(f):

    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.args.get('token', None)
        if token is None:
            return {"Message":"Your are missing Token"}
        else:
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
                return f(*args, **kwargs)
            except Exception as e:
                return {"Message":"Token is expired "}
    return decorator


class Controller(Resource):

    @verify_token
    def get(self):
        return "Hello this works"