# from modules.driver import Driver
from modules.driver2 import Driver
from config import ROBOT_ADDRESS
import math
import os


driver = None

try:
    # driver = Driver(ROBOT_ADDRESS)
    driver = Driver()
except Exception as ex:
    print(ex)
    os.sys.exit()

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
    driver.Beep()

# Point
def Zeigen():
    driver.point()

# Unpoint
def Nicht_zeigen():
    driver.unpoint()

# Calculate hypotenuse
def Hypotenuse(Länge, Höhe):
    Strecke = math.sqrt(Länge**2 + Höhe**2)
    Winkel = math.degrees(math.atan2(Höhe, Länge))
    return Strecke, Winkel