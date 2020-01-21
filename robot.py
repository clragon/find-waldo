if (True):
    from modules.driver_storm import Driver
else:
    from modules.driver_turtle import Driver

import math
import os


driver = None

try:
    driver = Driver()
except Exception as ex:
    print(ex)

# Left Motor
def Linker_Motor(Grad):
    driver.driveL(Grad)

# Right Motor
def Rechter_Motor(Grad):
    driver.driveR(Grad)

# Forward
def Beide_Motoren(Grad):
    driver.driveR(Grad)
    driver.driveL(Grad)

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
def Sprechen(Text):
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

# Define button press action
def Knopfdruck(Funktion, *Parameter):
    driver.btn_set(Funktion, *Parameter)