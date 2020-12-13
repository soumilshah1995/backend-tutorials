try:
    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse
    from flask_httpauth import HTTPBasicAuth
    import os
    import json
    import jwt
    import datetime
    import json
except Exception as e:
    print("Error Loading libraries : {} ".format(e))

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = '8ee2923d3cd2b2833d3b747173f6c0da'

USER_DATA = {
    "admin" : "admin"
}


@auth.verify_password
def verify(username,password):
    if not (username, password):
        return False
    return USER_DATA.get(username) == password


class LoginController(Resource):

    @auth.login_required
    def get(self):
        token = jwt.encode(
            {
                'user' : request.authorization.username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            }
        , app.config['SECRET_KEY'])

        return json.dumps({
            'token':token.decode('UTF-8')
        }, indent=3)

