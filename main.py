from robot import *
from image import *

Koordinaten = Finde_Person("docs/photo/marius.jpg", "docs/photo/tim-Gruppe_carlo.jpg")
Strecke, Winkel = Hypotenuse(Koordinaten)
Links(Winkel)
Vorwärts(Strecke)

