from shutil import copyfile
from robot import *
from image import *
import os

def robot():
    Vorwärts(10)
    Links(90)
    Vorwärts(10)
    Rückwärts(10)
    Rechts(90)
    Rückwärts(10)

    Strecke, Winkel = Hypotenuse(10, 10)
    Links(Winkel)
    Vorwärts(Strecke)
    Rechts(180)
    Vorwärts(Strecke)
    Rechts(180)
    Rechts(Winkel)


def images():
    for i in range(1,15):
        pic = "docs/imgs/{}.jpg".format(str(i))
        try: 
            coords = Finde_Waldo(pic)
            crop = Ausschneiden(coords, pic)
            copyfile(crop, "docs/imgs/{}_crop.jpg".format(str(i)))
        except:
            pass



def all():
    Koordinaten = Finde_Person("docs/photo/marius.jpg", "docs/photo/tim-Gruppe_carlo.jpg")
    Strecke, Winkel = Hypotenuse(Koordinaten)
    Links(Winkel)
    Vorwärts(Strecke - ROBOT_ARM_SIZE)
    Zeigen()
    sleep(3)
    Nicht_zeigen()
    Links(180)
    Vorwärts(Strecke - ROBOT_ARM_SIZE)
    Rechts(180 + Winkel)
