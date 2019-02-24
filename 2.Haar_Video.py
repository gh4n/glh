import cv2
import numpy as np
import os
from utils import cleanDir
dir = os.path.dirname(os.path.realpath(__file__))


def visitDir(path):
    if not os.path.isdir(path):
        print('Error: "', path, '" is not a directory or does not exist.')
        return
    else:
        global num
        try:
            for lists in os.listdir(path):
                sub_path = os.path.join(path, lists)
                num += 1
                # print('No.', x, ' ', sub_path)
                if os.path.isdir(sub_path):
                    visitDir(sub_path)
        except:
            pass


if __name__ == '__main__':

    FRAMES_DIR = dir + "/frames"
    FULLFRAME_OUTPUT_DIR = dir + "/detection_fullframe_output"
    CROPPED_OUTPUT_DIR = dir + "/detection_cropped_output"

    print("Cleaning output directories...")
    cleanDir(FULLFRAME_OUTPUT_DIR)
    cleanDir(CROPPED_OUTPUT_DIR)
    print("Done")

    side_view_face_cascade = cv2.CascadeClassifier(
        r"lbpcascade_profileface.xml"
    )

    frontal_face_cascade = cv2.CascadeClassifier(
        r"haarcascade_frontalface_default.xml"
    )

    num = 0
    path_list = []
    face_position_list = []
    no_face = None
    visitDir(FRAMES_DIR)
    for i in range(1, num):
        path_no = FRAMES_DIR + "/" + str(i) + ".png"
        path_list.append(path_no)
    for i in range(num-1):
        print(f"{i+1}/{num}")
        path = path_list[i]
        img = cv2.imread(path)

        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.equalizeHist(img2gray)
        # frontal_face_position = frontal_face_cascade\
        #     .detectMultiScale(img2gray, minNeighbors=5)
        frontal_face_position = frontal_face_cascade\
            .detectMultiScale(img2gray, 1.3, 5)

        if isinstance(frontal_face_position, np.ndarray):
            for (x,y,w,h) in frontal_face_position:
                # roi_gray = img2gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                cv2.imwrite(CROPPED_OUTPUT_DIR + "/" + str(i + 1) + ".png", roi_color)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.imwrite(FULLFRAME_OUTPUT_DIR + "/" + str(i + 1) + ".png", img)

        # if len(frontal_face_position) == 0:
        #     pass
        # elif len(frontal_face_position) == 2:
        #     frontal_face_position1 = frontal_face_position[1]
        #     # print(frontal_face_position1)
        #     x = frontal_face_position1[0]
        #     y = frontal_face_position1[1]
        #     w = frontal_face_position1[2]
        #     h = frontal_face_position1[3]
        #     print(i + 1, ":", x, y, w, h)
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #     cv2.imwrite(OUTPUT_DIR + "/" + str(i + 1) + ".png", img)
        #     face_position_list.append(frontal_face_position)
        # else:
        #     face_position_list.append(no_face)
    # print(face_position_list)

    # face_position_array = np.array(face_position_list).reshape(num, 1)

    # face = crop[y:y+h,x:x+w]
    # imageVar = cv2.Laplacian(image, cv2.CV_64F).var()

    # save1 = pd.DataFrame(face_position_array,
    #                      columns=['(X,Y),width,height'])
    # save1.to_csv('Face_Position_Video1.csv')
