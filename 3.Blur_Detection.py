#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import json
import logging

import cv2
import numpy

from detection import estimate_blur
from detection import fix_image_size

def find_images(input_dir):
    extensions = [".jpg", ".png", ".jpeg"]

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if os.path.splitext(file)[1].lower() in extensions:
                yield os.path.join(root, file)

dir = os.path.dirname(os.path.realpath(__file__))

INPUT_DIR = dir + "/detection_cropped_output"

logging.basicConfig(level=logging.INFO)

results = []

for input_path in find_images(INPUT_DIR):
    try:
        logging.info("processing {0}".format(input_path))
        input_image = cv2.imread(input_path)

        blur_map, score, blurry = estimate_blur(input_image)

        # logging.info("input_path: {0}, score: {1}, blurry: {2}".format(input_path, score, blurry))
        results.append({"input_path": input_path, "score": score, "blurry": blurry})

        #     cv2.imshow("input", input_image)
        #     cv2.imshow("result", pretty_blur_map(blur_map))
        #     cv2.waitKey(0)

    except Exception as e:
        print(e)
        pass

num_blurry = 0
total_score = 0
num_entries = 0

for entry in results:
    num_entries += 1
    total_score += entry["score"]
    if entry["blurry"]:
        num_blurry += 1

print(f"average score: {total_score / num_entries}")
print(f"blurry: {num_blurry}")
print(f"non-blurry: {num_entries-num_blurry}")
print(f"percentage: {num_blurry / num_entries * 100}")