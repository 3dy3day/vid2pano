import cv2
import numpy as np


def main(path):
    img = cv2.imread("./output/"+path)
    img = ((abs(cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)) +
                abs(cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3))) / 2).astype('uint8')

    cv2.imwrite("./output/(Edge)"+path, img)