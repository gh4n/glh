#! /bin/bash

if [ $# -ne 1 ]; then
    echo "No arguments supplied"
    exit 1 
fi

if [ ! -f $1 ]; then
    echo "File not found!"
    exit 1
fi

python 1.Frame_Cut.py -i "$1"
python 2.Haar_Video.py
python 3.Blur_Detection.py