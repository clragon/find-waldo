from robot import *
from image import *

import os

print("Bereiten sie die Webcam vor.")
print("Als Gruppe vor die Kamera stehen oder Bildpfad eingeben, dann enter drücken")
inp = input()
if (os.path.exists(inp):
    Gruppe = inp
else:
    Gruppe = Foto()
print("Einzelne Person vor Kamera stellen oder Bildpfad eingeben, enter drücken")
inp = input()
if (os.path.exists(inp):
    Person = inp
else:
    Person = Foto()
print("Das Gruppenfoto ausdrucken (Datei hier: {}) und die Breite in cm eingeben".format(Gruppe))
Breite = float(input())
print("Roboter bereitstellen, dann enter drücken")
input()
print("Finde Person...")
Pixel = Finde_Person(Person, Gruppe)
Zeige_Foto(Markieren(Pixel, Gruppe))
Koordinaten = Konvertieren(Pixel, Vergrössern(Gruppe, Breite))
Koordinaten = [Koordinaten[0] + ROBOT_ARM_SIZE / 10, Koordinaten[1], Koordinaten[2] + ROBOT_ARM_SIZE / 10, Koordinaten[3]]
Strecke, Winkel = Hypotenuse2(Koordinaten)

print("Fahre Roboter")
Rechts(Winkel)
Vorwärts(Strecke - ROBOT_ARM_SIZE/10)
Zeigen()
print("Ziel erreicht")
Sprechen("Target reached")
print("enter drücken um den Roboter zurückkehren zu lassen")
input()
Nicht_Zeigen()
Rückwärts(Strecke - ROBOT_ARM_SIZE/10)
Links(Winkel)
