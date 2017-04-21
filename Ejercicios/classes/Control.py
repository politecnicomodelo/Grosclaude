class Control(object):
    Peso = 0
    Altura = 0
    Fecha = None

    def SetControl(self,p,a,f):
        self.Peso = p
        self.Altura = a
        self.Fecha = f

    def MostrarControl(self):
        return self.Peso, self.Altura, self.Fecha
