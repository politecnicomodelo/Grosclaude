from .ServicioBordo import ServicioABordo
class Servicios(ServicioABordo):

    def __init__(self,n,a,fn,dni,m,i):
        ServicioABordo.__init__(self,n,a,fn,dni,m)
        self.Idiomas = []
        a = i.split(",")
        for item in a:
            self.Idiomas.append(item)