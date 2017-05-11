class Plato(object):

    def __init__(self,n,p):
        self.Nombre = n
        self.Precio = p

    def ModifPlato(self,n=None,p=None):
        if n:
            self.Nombre = n
        if p:
            self.Precio = p