print("1 -------------")
from robot import *
print("2 -------------")
from image import *

print("3 -------------")
LinkerMotor(100)
print("4 -------------")
RechterMotor(100)
print("5 -------------")

Foto()
print("6 -------------")
Zeige_Foto("docs/photo/webcam.jpg")

'''

print("7 -------------")

Pixel = Finde_Person("docs/photo/marius.jpg", "docs/photo/tim-Gruppe_carlo.jpg")
Koordinaten = Konvertieren(Pixel, Vergrössern("docs/photo/tim-Gruppe_carlo.jpg", 1000))

Strecke, Winkel = Hypotenuse2(Koordinaten)
Links(Winkel)
Vorwärts(Strecke - ROBOT_ARM_SIZE)
'''
