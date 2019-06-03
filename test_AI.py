#!/usr/bin/env python3
from modules.TFBrain import TFBrain
from PIL import Image
import os
import sys


def test_images():
    for i in range(1,15):
        image = Image.open('docs/imgs/'+str(i)+'.jpg')
        brain = TFBrain(image, 'models/frozen_inference_graph.pb')
        if brain.find_waldo() is True:
            print("Waldo found in {}.jpg".format(str(i)))
            image.crop(brain.get_waldo_box()).save("heads/waldo_"+str(i)+".jpg")
        else:
            sys.exit(-1)

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
    test_images()