import cv2
import numpy as np
import os
import ntpath
from detection import estimate_blur
from utils import cleanDir, find_images
dir = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':

    FRAMES_DIR = dir + "/frames"
    FULLFRAME_OUTPUT_DIR = dir + "/detection_fullframe_output"
    CROPPED_OUTPUT_DIR = dir + "/detection_cropped_output"
    ALLFRAME_OUTPUT_DIR = dir + "/detection_all_frames"

    print("Cleaning output directories...")
    cleanDir(FULLFRAME_OUTPUT_DIR)
    cleanDir(CROPPED_OUTPUT_DIR)

    print("Loading cascades...")

    side_view_face_cascade = cv2.CascadeClassifier(
        r"lbpcascade_profileface.xml"
    )

    frontal_face_cascade = cv2.CascadeClassifier(
        r"haarcascade_frontalface_default.xml"
    )

    print("Detecting faces...")

    num_images = 0
    for path in find_images(FRAMES_DIR):
        num_images += 1
        img = cv2.imread(path)
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.equalizeHist(img2gray)
        frontal_face_position = frontal_face_cascade\
            .detectMultiScale(img2gray, 1.3, 5)

        if isinstance(frontal_face_position, np.ndarray):
            for (x,y,w,h) in frontal_face_position:
                roi_gray = img2gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                cv2.imwrite(CROPPED_OUTPUT_DIR + "/" + str(num_images) + ".png", roi_color)

                blur_map, score, blurry = estimate_blur(roi_gray)
                if score < 100:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                
                # cv2.imwrite(FULLFRAME_OUTPUT_DIR + "/" + str(num_images) + ".png", img)

        cv2.imwrite(ALLFRAME_OUTPUT_DIR + "/" + ntpath.basename(path), img)
    
    print("Done!")