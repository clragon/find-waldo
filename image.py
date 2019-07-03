from modules.aws_brain import find_face
from modules.tf_brain import find_waldo
from modules.camera import take_photo
from PIL import Image, ImageDraw
from modules.robot_conf import *
from datetime import datetime
from shutil import copyfile


os.makedirs("Fotos", exist_ok=True)

def Foto():
    file = take_photo("Fotos/webcam.jpg"), CAMERA_ADDRESS, CAMERA_PORT)
    copyfile(file, "Fotos/webcam_{:%Y.%m.%d_%H-%M-%S}.jpg".format(__name__, datetime.now()))
    return file

def Finde_Person(Person, Gruppen_Foto):
    return find_face(Person, Gruppen_Foto)

def Finde_Waldo(Bild):
    return find_waldo(Bild)

def Markieren(Pixel, Gruppen_Foto):
    file = "Fotos/markiert.jpg"
    img = Image.open(Gruppen_Foto).convert("RGB")
    ImageDraw.Draw(img).rectangle(Pixel, outline="red", width=2)
    img.save(file, "JPEG")
    copyfile(file, "Fotos/webcam_{:%Y.%m.%d_%H-%M-%S}.jpg".format(__name__, datetime.now()))
    return file

def Ausschneiden(Pixel, Gruppen_Foto):
    file = "Fotos/ausgeschnitten.jpg"
    img = Image.open(Gruppen_Foto).convert("RGB").crop(Pixel)
    img.save(file, "JPEG")
    copyfile(file, "Fotos/webcam_{:%Y.%m.%d_%H-%M-%S}.jpg".format(__name__, datetime.now()))
    return file

def Zeige_Foto(Foto):
    Image.open(Foto).show()

def Konvertieren(Pixel, Vergrösserung):    
    return [round(num / Vergrösserung) for num in Pixel]

def Vergrössern(Bild, Ausdruck):
    return Image.open(Bild).width / Ausdruck


