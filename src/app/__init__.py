#pylint: skip-file
from flask import Flask
from flask_restful import Resource, Api
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import logging
import traceback

from .logger import configurar_logging

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
API = Api(app)
configurar_logging()

logger = logging.getLogger(__name__)

class HelloWorld(Resource):
    def get(self):
        # TODO poner en variable de entorno
        title = requests.get(
            'https://hello-world-node-taller2.herokuapp.com/').json()['title']
        logger.debug('debug de prueba')
        logger.info('info de prueba')
        logger.warn('warn de prueba')
        logger.error('error de prueba')
        return {'title': f'({title}) by Flask'}

class Rompe(Resource):
    def get(self):
        raise Exception('exception de prueba')

@app.errorhandler(Exception)
def unhandled_exception(e):
    tb = traceback.format_exc()
    logger.warn(f'Excepcion no manejada: {tb}')
    return {'mensaje': str(e)}, 500


API.add_resource(HelloWorld, '/')
API.add_resource(Rompe, '/rompe')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

logger.info(f'Iniciando version de la app: {Config.APP_VERSION}')
from app import models
