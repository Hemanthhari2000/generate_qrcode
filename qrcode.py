import cv2
import numpy as np

from pyzbar.pyzbar import decode

img = cv2.imread('1.png')
imgCopy = img.copy()
for barcode in decode(imgCopy):
    myData = barcode.data.decode('utf-8')
    print(myData)
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape(-1, 1, 2)
    cv2.polylines(imgCopy, [pts], True, (0, 255, 0), 4)

cv2.imshow('img', imgCopy)

cv2.waitKey(0)