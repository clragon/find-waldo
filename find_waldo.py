#!/usr/bin/env python3
from modules.AI import AI
from PIL import Image
import os

# def moveToWaldo():
#     # Initialize a robot and a driver for it.
#     print("Initialize Robot...")
#     robot = Robot(IP_ADDRESS)
#     print("DEBUG")
#     driver = Driver(robot)
#     # tell the driver to move to new coordniates.
#     x=20
#     y=20
#     print("Move robot to coordinates: {} {}".format(x,y))
#     driver.move(x, y, True)
#     driver.speak('I am pointing')
#     # tell the driver to drive back to it's original location.
#     driver.retreat()

def main():
    # Code here
    for i in range(1,38):
        image = Image.open('docs/imgs/'+str(i)+'.jpg')
        brain = AI(image)
        if brain.find_waldo() is True:
            print("Waldo found in {}.jpg".format(str(i)))
            image.crop(brain.get_waldo_box()).save("heads/waldo_"+str(i)+".jpg")
        else:
            print("Waldo not found in {}.jpg".format(str(i)))

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