#!/usr/bin/env python3

from awsHandler import get_position
from PIL import Image, ImageDraw

x_start, y_start, x_end, y_end = get_position("..\\docs\\imgs\\carlo.jpg", "..\\docs\\imgs\\tim-Gruppe1.jpg")

print("{} {} {} {}".format(x_start, y_start, x_end, y_end))

img = Image.open("..\\docs\\imgs\\tim-Gruppe1.jpg").convert("RGB")

draw = ImageDraw.Draw(img)
draw.rectangle([x_start, y_start, x_end, y_end], outline="red")

img.save("..\\docs\\imgs\\tim-Gruppe_carlo.jpg", "JPEG")