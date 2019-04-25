#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt

from modules.remote_robot import Robot
from brain import Brain
from modules.cam import Camera
from cam_config import CAMERA_URL
import numpy as np
from PIL import Image as PilImage


def find_waldo():
    # Distance from the center of the robot to the pointer
    pointer = 80
    image_height = 280

    print("Taking a picture...")
    cam = Camera()
    img = cam.take_snapshot(CAMERA_URL)
    if img is None:
        exit("No image recorde")

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

    # When arrived on the correct x coordinate, drive a litte further to set the pointer on this place
    x = x + pointer

    # Currently the robot drives backwards, reverse direction
    x = -x
    
    # Initialize and command the robot
    print("Initialize Robot...")
    robot = Robot("192.168.137.43")

    print("Move robot to coordinates: {} {}".format(x,y))
    robot.drive(y)
    robot.turn(90)
    robot.drive(x)
    print('Pointing')
    robot.point(True)
    robot.speak('I am pointing')
    time.sleep(3)
    robot.point(False)


if __name__ == '__main__':
    find_waldo()
