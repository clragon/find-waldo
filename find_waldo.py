#!/usr/bin/env python3

#import sys
#sys.path.insert(0, './modules')

from modules.remote_robot import Robot
from modules.cam import cam
from modules.image import Image


def find_waldo():
    print("Taking a picture...")
    img = cam()

    print("Recognizing Waldo and gettting coordinates...")
    Image(img)

    print("Initialize Robot...")
    robot = Robot("192.168.137.43")

    print("Move robot to coordinates...")
    robot.drive(20)

if __name__ == '__main__':
    find_waldo()