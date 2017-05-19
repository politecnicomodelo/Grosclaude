from .Personas import Persona
class ServicioABordo(Persona):

    def __init__(self,n,a,fn,dni,m):
        Persona.__init__(self,n,a,fn,dni)
        self.ModAvion = m