from .Persona import Persona
class Alumno(Persona):

    def __init__(self,n,ap,div,dni):
        Persona.__init__(self,n,ap,dni)
        self.Division = div

    def ModifPersona(self,n = None,ap = None,dni = None,div = None):
        Persona.ModifPersona(n,ap,dni)
        if div:
            self.Division = div