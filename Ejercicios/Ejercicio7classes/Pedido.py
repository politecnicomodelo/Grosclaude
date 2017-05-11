from .Plato import Plato
class Pedido(object):

    def __init__(self,f,p,h,plato):
        self.FechaCreacion = f
        self.Persona = p
        self.HoraEnt = h
        self.Plato = plato
        self.Entregado = False

    def CalcularPrecio(self):
        (100-(self.Persona.GetDesc()))/100*self.Plato.Precio

    def ModifPedido(self,f=None,p=None,h=None,plato=None,ent=None):
        if f:
            self.FechaCreacion = f
        if p:
            self.Persona = p
        if h:
            self.HoraEnt = h
        if plato:
            self.Plato = plato
        if ent:
            self.Entregado = ent
