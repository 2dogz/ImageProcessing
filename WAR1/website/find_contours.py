from cv2 import cv2
import numpy as np
import time


def contoursPicture():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for data in contours:
            print("The contours have this data %r" %data)
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
        cv2.imwrite(f"static/photos/xyz.png", image)
    # If captured image is corrupted, moving to else part
    else:
        raise Exception("No image detected. Please! try again")
