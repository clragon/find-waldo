#!/usr/bin/env python3

import sys
sys.path.insert(0, './modules')

from modules.remote_robot import robot_go
from modules.cam import cam
from modules.image import Image


def find_waldo():
    print("Taking a picture...")
    img = cam()

    print("Recognizing Waldo and gettting coordinates...")
    Image(img)

    print("Initialize Robot...")


    print("Move robot to coordinates...")
    robot_go(10, 20)

if __name__ == '__main__':
    find_waldo()