class Persona(object):

    def __init__(self,n,ap,dni):
        self.Nombre = n
        self.Apellido = ap
        self.dni = dni

    def GetDesc(self):
        return 0

    def ModifPersona(self,n=None,ap=None,dni=None):
        if n!=None:
            self.Nombre = n
        if ap!=None:
            self.Apellido = ap
        if dni!=None:
            self.dni = dni
