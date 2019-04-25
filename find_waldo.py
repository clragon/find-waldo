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
    print("Taking a picture...")
    cam = Camera()
    img = cam.take_snapshot(CAMERA_URL)
    if img is None:
        exit("No image recorde")

    print("Rec Waldo...")    
    brain = Brain(False, "model2_10200epochs.h5")
    result = brain.find_waldo(img)
    if result is None:
        exit("Waldo not found")

    print("Result from Brain: {}".format(result))

    print("Initialize Robot...")
    robot = Robot("192.168.137.43")

    print("Move robot to coordinates...")
    robot.drive(20)
    # robot.turn(45)
    # robot.turn(-45)
    # robot.drive(-100)
    print('Pointing')
    robot.point(True)
    robot.speak('I am pointing')
    time.sleep(3)
    robot.point(False)


if __name__ == '__main__':
    find_waldo()
