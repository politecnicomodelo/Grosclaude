from .Personas import Persona
class Pasajero(Persona):

    def __init__(self,n,a,fn,dni,vip,ne = None):
        Persona.__init__(self,n,a,fn,dni)
        self.Vip = vip
        self.Necesidades = ne

