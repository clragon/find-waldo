#!/usr/bin/env python3

import os
from image import *
from robot import *
from robot_conf import *
from time import sleep


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
    Koordinaten = Finde_Person("docs/photo/marius.jpg", "docs/photo/tim-Gruppe_carlo.jpg")
    Strecke, Winkel = Hypotenuse(Koordinaten)
    Links(Winkel)
    Vorwärts(Strecke - ROBOT_ARM_SIZE)
    Zeigen()
    sleep(3)
    Nicht_zeigen()
    Links(180)
    Vorwärts(Strecke - ROBOT_ARM_SIZE)
    Rechts(180 + Winkel)


def _distance(self, source, target):
    return self._pixel_to_millimeters(abs(target-source))

def _pixel_to_millimeters(self, pixel_range):
    scale_factor = self.source_image.get_scale_factor()
    return pixel_range/scale_factor


if __name__ == '__main__':
    os.makedirs("heads", exist_ok=True)
    find_face()
