from modules.aws_brain import find_face
from modules.tf_brain import find_waldo
from modules.camera import take_photo
from PIL import Image, ImageDraw

from robot_conf import *

def Foto():
    return take_photo(CAMERA_ADDRESS, CAMERA_PORT)

def Finde_Person(Person, Gruppen_Foto):
    return find_face(Person, Gruppen_Foto)

def Finde_Waldo(Bild):
    return find_waldo(Bild)

def Markieren(Pixel, Gruppen_Foto):
    file = "docs/photo/markiert.jpg"
    img = Image.open(Gruppen_Foto).convert("RGB")
    ImageDraw.Draw(img).rectangle(Pixel, outline="red", width=2)
    img.save(file, "JPEG")
    return file

def Ausschneiden(Pixel, Gruppen_Foto):
    file = "docs/photo/ausgeschnitten.jpg"
    img = Image.open(Gruppen_Foto).convert("RGB").crop(Pixel)
    img.save(file, "JPEG")
    return file

def Zeige_Foto(Foto):
    Image.open(Foto).show()

def Konvertieren(Pixel, Vergrösserung):    
    return [round(num / Vergrösserung) for num in Pixel]

def Vergrössern(Bild, Ausdruck):
    return Image.open(Bild).width / Ausdruck


