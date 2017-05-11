from .Persona import Persona
class Profesor(Persona):

    def __init__(self,n,ap,dni):
        Persona.__init__(self,n,ap,dni)
        self.Descuento = 30

    def GetDesc(self):
        return self.Descuento

    def ModifProf(self,n = None,ap = None,dni=None,des = None):
        Persona.ModifPersona(n,ap,dni)
        if des:
            self.Descuento = des
