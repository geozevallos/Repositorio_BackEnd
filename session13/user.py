import db

from sqlalchemy import Column, Integer, String



# Modelando los campos de la BD
class User(db.Base):
    __tablename__ = 'user'
    iduser = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(String)
    telefono = Column(String)
    correo = Column(String)
