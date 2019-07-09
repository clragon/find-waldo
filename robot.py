from modules.driver import Driver  
# from modules.driver2 import Driver 

from modules.robot_conf import ROBOT_ADDRESS
import math
import os



driver = None

try:
    driver = Driver(ROBOT_ADDRESS)
except Exception as ex:
    print(ex)
    os.sys.exit()

# LinkerMotor
def LinkerMotor(grad):
    driver.driveL(grad)

# RechterMotor
def RechterMotor(grad):
    driver.driveR(grad)

# VorwärtsGrad
def BeideMotoren(grad):
    driver.driveR(grad)
    driver.driveL(grad)

# Forward
def Vorwärts(cm):
    driver.drive(cm * 10)

# Backwards
def Rückwärts(cm):
    driver.drive(-(cm * 10))

# Turn right
def Rechts(Grad):
    driver.turn(Grad)

# Turn left
def Links(Grad):
    driver.turn(-Grad)

# Speak
def Sprich(Text):
    driver.speak(Text)

# Beep
def Beep():
    driver.beep()

# Point
def Zeigen():
    driver.point()

# Unpoint
def Nicht_Zeigen():
    driver.unpoint()

# Calculate hypotenuse
def Hypotenuse(Länge, Höhe):
    Strecke = math.sqrt(Länge**2 + Höhe**2)
    Winkel = math.degrees(math.atan2(Höhe, Länge))
    return Strecke, Winkel

# Calculate hypotenuse with coordinates tuple
def Hypotenuse2(Koordinaten):
    return Hypotenuse(Koordinaten[0] + ((Koordinaten[2] - Koordinaten[0]) / 2), Koordinaten[1] + ((Koordinaten[3] - Koordinaten[1]) / 2))