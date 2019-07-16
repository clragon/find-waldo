from robot import *
from image import *

Person = "docs/pics/Person2.jpg"
Gruppe = "docs/pics/Gruppe.jpg"
Breite = 73.5
Pixel = Finde_Person(Person, Gruppe)
Koordinaten = Konvertieren(Pixel, Vergrössern(Gruppe, Breite))
Strecke, Winkel = Hypotenuse2(Koordinaten)
print("Coords: {}".format(Koordinaten))
print("Angle: {}".format(Winkel))
print("Distance: {}".format(Strecke - ROBOT_ARM_SIZE / 10))

Rechts(Winkel)
Vorwärts(Strecke - ROBOT_ARM_SIZE/10)
Zeigen()
Sprich("Person gefunden")
print("enter to return")
input()
Nicht_Zeigen()
Rückwärts(Strecke - ROBOT_ARM_SIZE/10)
Links(Winkel)
