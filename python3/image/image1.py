#!/usr/bin/env python3


from PIL import Image

image = Image.open("image1.png")
width, height = image.size

print("Width:", width)
print("Height:", height)
