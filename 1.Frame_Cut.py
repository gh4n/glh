import cv2
import os
import argparse
from utils import cleanDir

dir = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = dir + '/frames'

parser = argparse.ArgumentParser(description='Cut up a video into individual frames')
parser.add_argument('-i', '--input_file', dest="input_file", type=str, required=True, help="path to input file")

args = parser.parse_args()


print("Cleaning output directory...")
cleanDir(OUTPUT_DIR)

print("Reading video...")
vidObj = cv2.VideoCapture(args.input_file) 
count = 1

# checks whether frames were extracted 
success = 1

while success and count < 700: 
    # vidObj object calls read 
    # function extract frames 
    success, image = vidObj.read() 

    # Saves the frames with frame-count 
    cv2.imwrite(OUTPUT_DIR + "/%d.png" % count, image) 

    count += 1
  
print("Done!")