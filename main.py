from robot import *
from image import *

print("Bereiten sie die Webcam vor.")
print("Als Gruppe vor die Kamera stehen, dann enter drücken")
input()
Gruppe = Foto()
print("Einzelne Person vor Kamera stellen, enter drücken")
input()
Person = Foto()
print("Das Gruppenfoto ausdrucken (Datei hier: {}) und die Breite in cm eingeben")
Breite = int(input())
print("Roboter bereitstellen, dann enter drücken")
input()
print("Finde Person...")
Pixel = Finde_Person(Person, Gruppe)
Koordinaten = Konvertieren(Pixel, Vergrössern(Gruppe, Breite))
print("Fahre Roboter")
Strecke, Winkel = Hypotenuse2(Koordinaten)
Links(Winkel)
Vorwärts(Strecke - ROBOT_ARM_SIZE)
Zeigen()
Sprich("Person gefunden")

