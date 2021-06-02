from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


# Quiero usar e moto SQl, y la interfaz de python con mysql
# Ingesar usuario:contraseña - @localhost/nombredelabasededatos
engine = create_engine("mysql+pymysql://root:admin@localhost/usersdb")

# Crear el objeto, clase para modelar las tablas
Base = declarative_base()

#Crear una sesion, y decir que está enlazado con el motor engine
#Esto representa transacciones
Session = sessionmaker(bind=engine)