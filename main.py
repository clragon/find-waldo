from robot import *
from image import *


Pixel = Finde_Person("docs/Fotos/Person.jpg", "docs/Fotos/Gruppe.jpg")
Koordinaten = Konvertieren(Pixel, Vergrössern("docs/Fotos/Gruppe.jpg", 1000))

Strecke, Winkel = Hypotenuse2(Koordinaten)
Links(Winkel)
Vorwärts(Strecke - ROBOT_ARM_SIZE)

