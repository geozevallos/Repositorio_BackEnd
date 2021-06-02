
from ZOO.controllers.zoo_animal_controller import ZooAnimalController
from ZOO.controllers.zoo_animals_controller import ZooAnimalsController
from ZOO.controllers.zoos_controller import ZoosController
from ZOO.controllers.helloController import HelloController

from flask import Flask
from flask_restful import Api



# Flaskrestfull para las rutas
#Un recurso es una representación de un objeto en la vida real

app = Flask(__name__)
api = Api(app)


#En esta api quiero registrar un nuevo recurso y la ruta con la q va a acceder
api.add_resource(HelloController, '/hello')
api.add_resource(ZoosController, '/zoos')
api.add_resource(ZooAnimalsController, '/zoo/<int:zoo_id>/animals')
api.add_resource(ZooAnimalController, '/zoo/<int:zoo_id>/animal/<int:animal_id>') #animal especifico


#Esto era antes sin el restful
# @app.route('/')
# def index():
#     return "Hola, bebé ;)"