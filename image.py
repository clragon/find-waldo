from modules.aws_brain import find_face
from modules.camera import take_photo
from PIL import Image, ImageDraw
from modules.robot_conf import *
import tkinter, tkinter.filedialog
from datetime import datetime
from shutil import copyfile
import os


os.makedirs("Fotos", exist_ok=True)

def Foto():
    default = take_photo(("Fotos/webcam.jpg"), CAMERA_ADDRESS, CAMERA_PORT)
    file = "Fotos/webcam_{}.jpg".format(datetime.now().strftime("%Y.%m.%d_%H-%M-%S"))
    copyfile(default, file)
    return file

def Finde_Person(Person, Gruppen_Foto):
    return find_face(Person, Gruppen_Foto)

def Markieren(Pixel, Gruppen_Foto):
    default = "Fotos/markiert.jpg"
    file = "Fotos/markiert_{}.jpg".format(datetime.now().strftime("%Y.%m.%d_%H-%M-%S"))
    img = Image.open(Gruppen_Foto).convert("RGB")
    ImageDraw.Draw(img).rectangle(Pixel, outline="red", width=3)
    img.save(default, "JPEG")
    copyfile(default, file)
    return file

def Ausschneiden(Pixel, Gruppen_Foto):
    default = "Fotos/ausgeschnitten.jpg"
    file = "Fotos/ausgeschnitten_{}.jpg".format(datetime.now().strftime("%Y.%m.%d_%H-%M-%S"))
    img = Image.open(Gruppen_Foto).convert("RGB").crop(Pixel)
    img.save(default, "JPEG")
    copyfile(default, file)
    return file

def Wähle_Foto():
    root = tkinter.Tk().withdraw()
    return tkinter.filedialog.askopenfilename(initialdir = "./Fotos/", title = "Bild auswählen", filetypes = (("jpeg files", "*.jpg"),("all files", "*.*")))

def Zeige_Foto(Foto):
    Image.open(Foto).show()

def Konvertieren(Pixel, Vergrösserung):    
    return [round(num / Vergrösserung) for num in Pixel]

def Vergrössern(Bild, Ausdruck):
    return Image.open(Bild).width / Ausdruck


