class Mascota(object):
    nombre=""
    tipo=""
    def setNombre(self,n):
        self.nombre=n
    def setTipo(self,t):
        self.tipo=str(t)
    def quienSoy(self):
        return "Soy " + self.nombre + " un " +self.tipo
