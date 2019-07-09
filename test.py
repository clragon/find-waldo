from robot import *
from image import *

Person = "docs/pics/Person.jpg"
Gruppe = "docs/pics/Gruppe.jpg"
Breite = 83.5
Pixel = Finde_Person(Person, Gruppe)
Koordinaten = Konvertieren(Pixel, Vergrössern(Gruppe, Breite))
# hack to increase distance
Koordinaten = [Koordinaten[0] + ROBOT_ARM_SIZE / 10, Koordinaten[1], Koordinaten[2] + ROBOT_ARM_SIZE / 10, Koordinaten[3]]
Strecke, Winkel = Hypotenuse2(Koordinaten)
print("Coords: {}".format(Koordinaten))
print("Angle: {}".format(Winkel))
print("Distance: {}".format(Strecke - ROBOT_ARM_SIZE / 10))

test = "docs/pics/test.jpg"
img = Image.open(Gruppe).convert("RGB")
pix = (Pixel[0] + ((Pixel[2] - Pixel[0]) / 2), Pixel[1] + ((Pixel[3] - Pixel[1]) / 2))
ImageDraw.Draw(img).line(((0, 0), pix), fill="red", width=3)
img.save(test, "JPEG")
# Zeige_Foto(Markieren(Pixel, test))

Rechts(Winkel)
Vorwärts(Strecke - ROBOT_ARM_SIZE/10)
Zeigen()
Sprich("Person gefunden")
print("enter to return")
input()
Nicht_Zeigen()
Rückwärts(Strecke - ROBOT_ARM_SIZE/10)
Links(Winkel)
