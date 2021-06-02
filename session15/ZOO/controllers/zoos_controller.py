from sqlalchemy.sql.expression import select
from ZOO.models.zoo import Zoo
from ZOO.database import Session
from flask_restful import Resource
from flask import request
from flask import jsonify

#Este controlador es un recurso
class ZoosController(Resource):
    # Listar zoologicos
    def get(self):
        # session = Session()
        zoos = select(Zoo)
        return jsonify(zoos)


    #Crear zoologicos
    def post(self):
        # Iniciar la sesion
        session = Session()

        # Recibir la información
        data = request.json

        #Crear una instancia del modelo, lo q sería un registro
        zoo = Zoo()
        # zoo.idzoo = data["idzoo"]
        zoo.nombre = data["nombre"]
        zoo.ciudad = data["ciudad"]
        zoo.tamanioM2 = data["tamanioM2"]
        zoo.presupuestoAnual = data["presupuestoAnual"]

        session.add(zoo)
        session.commit()

        return "OK", 201
           