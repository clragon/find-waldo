#!/usr/bin/env python3
from modules.tf_brain import TFBrain
from PIL import Image
import os
import sys


def test_images():
    for i in range(1,15):
        image = Image.open('docs/imgs/{}.jpg'.format(str(i)))
        brain = TFBrain(image, 'models/frozen_inference_graph.pb')
        if brain.find_waldo() is True:
            print("Waldo found in {}.jpg".format(str(i)))
            image.crop(brain.get_box())
            image.save("heads/waldo_{}.jpg".format(str(i)))
        else:
            pass

if __name__ == '__main__':
    os.makedirs("heads", exist_ok=True)
    test_images()