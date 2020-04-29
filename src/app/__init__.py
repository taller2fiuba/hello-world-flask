#pylint: skip-file
from flask import Flask
from flask_restful import Resource, Api
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
API = Api(app)


class HelloWorld(Resource):
    def get(self):
        # TODO poner en variable de entorno
        title = requests.get(
            'https://hello-world-node-taller2.herokuapp.com/').json()['title']
        return {'title': f'({title}) by Flask'}


API.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from app import models
