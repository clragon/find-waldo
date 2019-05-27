#!/usr/bin/env python3
from modules.AI import AI
from PIL import Image
from config import IP_ADDRESS
from modules.remote_robot import Robot as RemoteRobot
from modules.Robot import Robot
import os


def move_to_wally(robot, x, y):
    robot.move_to(x, y)
    robot.retreat()
    robot.reset()


def search_wally(image):
    brain = AI(image,'models/frozen_inference_graph.pb')
    if brain.find_waldo() is True:
        (x, y) = brain.get_waldo_coords()
        print("Waldo found! at ({}.{})".format(x, y))
        return (x, y)
    else:
        print("Waldo not found")
        return (50, 50)


def setup_robot(scale_factor):
    # initialize the robot
    return Robot(RemoteRobot(IP_ADDRESS), scale_factor)


def main():
    # Code here
    image=Image.open("docs/imgs/3.jpg")
    (width,height)=image.size
    # 310 is the A3 size
    scale_factor = (width/410)

    robot = setup_robot(scale_factor)
    (x, y) = search_wally(image)
    move_to_wally(robot, x, y)


################################
# Don't change the code below
#
if __name__ == '__main__':
    try:
        os.mkdir("heads")
        print("Directory heads created")
    except OSError:
        print("Directory heads already initialized")
        pass
    main()
