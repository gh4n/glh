import cv2
import os
import argparse
from utils import cleanDir
dir = os.path.dirname(os.path.realpath(__file__))

OUTPUT_DIR = dir + '/frames'

parser = argparse.ArgumentParser(description='Cut up a video into individual frames')
parser.add_argument('-i', '--input_file', dest="input_file", type=str, required=True, help="path to input file")

args = parser.parse_args()

cleanDir(OUTPUT_DIR)

vc = cv2.VideoCapture(args.input_file)  # 读入视频文件
c = 1

if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
    print("Read Successfully")

else:
    rval = False

# timeF = 2  # 视频帧计数间隔频率
count = 0
name_no = 0
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    count += 1
    if count >= 0 & count < 500:
        if (count % 3 == 0):  # 每隔timeF帧进行存储操作
            name_no += 1
            # frame = frame[100:380, :]
            # frame = frame[100:350, :]
            try:
                filepath = OUTPUT_DIR + '/' + str(name_no) + '.png'
                print("wrote " + filepath)
                cv2.imwrite(filepath, frame)  # 存储为图像        cv2.waitKey(1)
            except:
                print("Failed write")
vc.release()
