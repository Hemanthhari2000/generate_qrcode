import cv2
import numpy as np
import os

from pyzbar.pyzbar import decode
import pyqrcode
from pyqrcode import QRCode
import png
import imutils

GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
RED = (0, 0, 255)

ROOT_DIR = os.getcwd()

IMG = '1.png'

IMG_PATH = os.path.join(ROOT_DIR, 'assets/inputs/'+ IMG)
OUT_PATH = os.path.join(ROOT_DIR, 'assets/outputs/output.png')


def resize(img, width=400):
    return imutils.resize(img, width)

def decodeQR(inp_path,out_path):
    img = cv2.imread(inp_path)

    img = resize(img)

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape(-1, 1, 2)
        cv2.polylines(img, [pts], True, BLUE, 4)

    # cv2.imshow('img', imgCopy)
    cv2.imwrite(out_path, img)
    # cv2.waitKey(0)    
    return str(myData)

def genQR(data):
    url = pyqrcode.create(data)
    url.png(OUT_PATH, scale = 10)
    return

def main():
    img = cv2.imread(IMG_PATH)
    imgCopy = img.copy()

    imgCopy = resize(imgCopy)

    for barcode in decode(imgCopy):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape(-1, 1, 2)
        cv2.polylines(imgCopy, [pts], True, BLUE, 4)

    cv2.imshow('img', imgCopy)

    cv2.waitKey(0)

# main()
# genQR("HELLO HEMANTH")