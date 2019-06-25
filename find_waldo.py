#!/usr/bin/env python3

import os
from config import *
from modules.tf_brain import TFBrain as Brain
from modules.aws_brain import AWSBrain
from modules.driver import Driver
from modules.camera import Camera
from robot import Robot

from PIL import Image


def find_waldo():
    target_image = Image.open("docs/imgs/1.jpg")
    # Setup the Robot
    # Setup the brain
    brain = Brain(target_image, 'models/frozen_inference_graph.pb')
    if brain.find_waldo() is True:
        (x, y) = brain.get_coords()
        target_image.set_scale_factor()
        # Move to Wally
        robot = Robot()
        robot.move_to(x, y)
        robot.retreat()
        robot.reset()
    else:
        os.sys.exit()


def find_face():
    # source face
    cam = Camera(CAMERA_ADDRESS)
    cam.take_photo()
    group_image = Image.open("docs/photo/ti8m-group.jpg")

    aws_brain = AWSBrain(cam, group_image)
    if aws_brain.find_face():
        (x, y) = aws_brain.get_coords()
        # move the robot here 748.0361535549164, 1389.703828215599
        Image.open("docs/photo/ti8m-group.jpg").mark(aws_brain.get_box())
        robot = Robot()
        robot.move_to(x, group_image.get_height()-y)
        robot.retreat()
        robot.reset()
    else:
        os.sys.exit()


def _distance(self, source, target):
    return self._pixel_to_millimeters(abs(target-source))

def _pixel_to_millimeters(self, pixel_range):
    scale_factor = self.source_image.get_scale_factor()
    return pixel_range/scale_factor


if __name__ == '__main__':
    os.makedirs("heads", exist_ok=True)
    find_face()
