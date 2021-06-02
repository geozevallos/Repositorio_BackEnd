

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Float, Integer, String
from ZOO.database import Base


class Zoo(Base):
    __tablename__ = 'zoo'

    idzoo = Column(Integer, primary_key=True)
    nombre = Column(String)
    ciudad = Column(String)
    tamanioM2 = Column(Float)
    presupuestoAnual = Column(Float)