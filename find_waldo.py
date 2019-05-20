#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt

from modules.remote_robot import Robot
from brain import Brain
from modules.cam import Camera
from modules.driver import Driver
from cam_config import CAMERA_URL
import numpy as np
from PIL import Image as PilImage
from config import *

def searchWaldo():
    print("start finding waldo...")  
    image_height = 280

    #print("Taking a picture...")
    #cam = Camera()
    #img = cam.take_snapshot(CAMERA_URL)
    #if img is None:
    #    exit("No image recorde")

    print("load image from folder...") 
    img = PilImage.open('docs/last_photo.jpg')
    # img.show()

    print("Rec Waldo...")    
    brain = Brain(False, "model2_10200epochs.h5")
    result = brain.find_waldo(img)
    result = (400, 120)
    if result is None:
        exit("Waldo not found")
    x,y = result
    print("Result from Brain: {} {}".format(x,y))

    # Transform camera coordinates to printed image coordinates

    # Origin is in the lower left corner instead in the upper left
    y = image_height - y

    # Currently the robot drives backwards, reverse direction
    y = -y
    x = -x
    return (20,20)

def searchFakeWaldo():
    return (20,20)

def moveToWaldo():
    # Initialize a robot and a driver for it.
    print("Initialize Robot...")
    robot = Robot(IP_ADDRESS)
    print("DEBUG")
    driver = Driver(robot)
    # tell the driver to move to new coordniates.
    x=20
    y=20
    print("Move robot to coordinates: {} {}".format(x,y))
    driver.move(x, y, True)
    driver.speak('I am pointing')
    # tell the driver to drive back to it's original location.
    driver.retreat()

def find_waldo():
    (x,y) = searchWaldo()
    
    print("Waldo coordinates")
    print("X = " + str(x))
    print("Y = " + str(y))
    # moveToWaldo()

if __name__ == '__main__':
    find_waldo()
