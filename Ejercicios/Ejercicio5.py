from datetime import date
from classes.Persona import Persona
from classes.Control import Control
p = Persona()
p.SetPersona("Pepe","Gomez",date(1994/12/3))
c = Control()
c.SetControl("49",105,date(2000/6/12))
p.AniadirControl(c)
