from flask_restful import Resource


from flask_restful import Resource

#Este controlador es un recurso
class HelloController(Resource):
    def get(self):
        return "hello world"