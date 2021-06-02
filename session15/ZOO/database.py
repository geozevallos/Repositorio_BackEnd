from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


#Tengo q decirle para crear el motor
engine = create_engine(
    "mysql+pymysql://adminzoo:adminzoo@localhost/zoologicosdb"
)

# el base para crear mis clases
Base = declarative_base()


#Necesito estar en una transacción en base a la session
#Cada petición es una sessión
Session = sessionmaker(bind=engine)