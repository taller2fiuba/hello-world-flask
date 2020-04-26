from flask import Flask
from flask_restful import Resource, Api
import requests

APP = Flask(__name__)
API = Api(APP)


class HelloWorld(Resource):
    def get(self):
        # TODO poner en variable de entorno
        title = requests.get(
            'https://hello-world-node-taller2.herokuapp.com/').json()['title']
        return {'title': f'({title}) by Flask'}


API.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)
