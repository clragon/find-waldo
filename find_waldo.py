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


def find_waldo():
    print("start finding waldo...")  
    image_height = 280

    #print("Taking a picture...")
    #cam = Camera()
    #img = cam.take_snapshot(CAMERA_URL)
    #if img is None:
    #    exit("No image recorde")

    print("load image from folder...") 
    img = PilImage.open('photo01.png')
    img.show()

    print("Rec Waldo...")    
    brain = Brain(False, "model2_10200epochs.h5")
    result = brain.find_waldo(img)
    #result = (400, 120)
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
    
    # Initialize a robot and a driver for it.
    print("Initialize Robot...")
    robot = Robot(IP_ADDRESS)

    driver = Driver(robot)

    # tell the driver to move to new coordniates.
    print("Move robot to coordinates: {} {}".format(x,y))
    driver.move(x, y, True)
    driver.speak('I am pointing')
    # tell the driver to drive back to it's original location.
    driver.retreat()


if __name__ == '__main__':
    find_waldo()
