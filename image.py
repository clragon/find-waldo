from modules.aws_brain import find_face
from modules.camera import Camera
from PIL import Image, ImageDraw
from robot_conf import *

def Foto():
    return Camera.take_photo(CAMERA_ADDRESS, CAMERA_PORT)

def Finde_Person(Person, Gruppen_Foto):
    return find_face(Person, Gruppen_Foto)

def Markieren(Koordinaten, Gruppen_Foto):
    file = "docs/photo/markiert.jpg"
    img = Image.open(Gruppen_Foto).convert("RGB")
    ImageDraw.Draw(img).rectangle(Koordinaten, outline="red", width=2)
    img.save(file, "JPEG")
    return file

def Ausschneiden(Koordinaten, Gruppen_Foto):
    file = "docs/photo/ausgeschnitten.jpg"
    img = Image.open(Gruppen_Foto).convert("RGB").crop(Koordinaten)
    img.save(file, "JPEG")
    return file

def Zeige_Foto(Foto):
    Image.open(Foto).show()


