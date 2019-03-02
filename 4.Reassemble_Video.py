
import os
import cv2
import numpy as np
import ntpath
from utils import find_images, sort_nicely
# encoding: UTF-8

dir = os.path.dirname(os.path.realpath(__file__))
INPUT_DIR = dir + "/detection_all_frames"
OUTPUT_FILENAME = "output.mp4"
OUTPUT_FILEPATH = dir + "/" + OUTPUT_FILENAME

print("Cleaning output files...")
if os.path.isfile(OUTPUT_FILEPATH):
    os.unlink(OUTPUT_FILEPATH)

print("Reading images...")
img_paths = []
for img_path in find_images(INPUT_DIR):
    
    img_paths.append(ntpath.basename(img_path))

sort_nicely(img_paths)

print("Writing " + OUTPUT_FILENAME + "...")

height, width, layers = cv2.imread(INPUT_DIR + "/" + img_paths[0]).shape
size = (width,height)
writer = cv2.VideoWriter(OUTPUT_FILENAME, cv2.VideoWriter_fourcc(*'MP4V'), 30, size)

for img_path in img_paths:
    img = cv2.imread(INPUT_DIR + "/" + img_path)
    writer.write(img)

writer.release()

# height , width , layers =  cv2.imread(INPUT_DIR + '/1.jpg').shape

# videoWriter = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 30, (1920, 1080))


# for img_path in find_images(INPUT_DIR):
#     img = cv2.imread(img_path)
#     videoWriter.write(img)