from robot import *
from image import *

print("Bereiten sie die Webcam vor.")
print("Als Gruppe vor die Kamera stehen, dann enter drücken")
# input()
# Gruppe = Foto()
Gruppe = "docs/pics/Gruppe.jpg"
print("Einzelne Person vor Kamera stellen, enter drücken")
# input()
# Person = Foto()
Person = "docs/pics/Person.jpg"
print("Das Gruppenfoto ausdrucken (Datei hier: {}) und die Breite in cm eingeben".format(Gruppe))
# Breite = int(input())
Breite = 42
print("Roboter bereitstellen, dann enter drücken")
print("Finde Person...")
Pixel = Finde_Person(Person, Gruppe)
# Zeige_Foto(Markieren(Pixel, Gruppe))
Koordinaten = Konvertieren(Pixel, Vergrössern(Gruppe, Breite))
print(Koordinaten)
Koordinaten = [Koordinaten[0] + ROBOT_ARM_SIZE / 10, Koordinaten[1], Koordinaten[2] + ROBOT_ARM_SIZE / 10, Koordinaten[3]]
Strecke, Winkel = Hypotenuse2(Koordinaten)
print(Winkel)
print(Strecke - ROBOT_ARM_SIZE / 10)

img = Image.open(Gruppe).convert("RGB")
pix = (Pixel[0] + ((Pixel[2] - Pixel[0]) / 2), Pixel[1] + ((Pixel[3] - Pixel[1]) / 2))
ImageDraw.Draw(img).line(((0, 0), pix), fill="red", width=3)
img.save("docs/pics/test.jpg", "JPEG")
Zeige_Foto("docs/pics/test.jpg")

print("Fahre Roboter")
Rechts(Winkel)
Vorwärts(Strecke - ROBOT_ARM_SIZE/10)
Zeigen()
Sprich("Person gefunden")
print("enter drücken um den Roboter zurückkehren zu lassen")
input()
Nicht_Zeigen()
Rückwärts(Strecke - ROBOT_ARM_SIZE/10)
Links(Winkel)
