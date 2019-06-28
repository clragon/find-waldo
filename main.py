from robot import *
from image import *

Pixel = Finde_Person("docs/photo/marius.jpg", "docs/photo/tim-Gruppe_carlo.jpg")
Koordinaten = Konvertieren(Pixel, Vergrösserung("docs/photo/tim-Gruppe_carlo.jpg", 1000))

Strecke, Winkel = Hypotenuse(Koordinaten)
Links(Winkel)
Vorwärts(Strecke - ROBOT_ARM_SIZE)
