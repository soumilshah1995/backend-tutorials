try:
    from api import (app,api,LoginController,Controller)
except Exception as e:
    print("Error : {} ".format(e))

api.add_resource(LoginController, '/login')
api.add_resource(Controller, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')