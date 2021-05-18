from datetime import datetime

class Spy:

    nombre = "unknown"
    ultima_modificacion: datetime.now

    def __setattr__(self, att,val):
        print("actualizando nombre a " + val)
        self.nombre = val
    

espia = Spy()
espia.nombre = "James Bond"