import cv2
import numpy as np

#TUTORIAL SOURCE : https://docs.opencv.org/4.5.1/dc/dbb/tutorial_py_calibration.html
def chessboardPicture():
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

     #DEFAULT CAMERA PORT
    cam_port = 0

    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6*7,3), np.float32)
    objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

    cam = cv2.VideoCapture(cam_port)

    # set resolution
    cam.set(3, 1920)
    cam.set(4, 1080)

    # print resolutions - debug
    width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(width, height)

    # reading the input using the camera
    result, image = cam.read()
    if result:
        cv2.imwrite("static/photos/input.png", image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (9,6), None)
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners)
            cv2.drawChessboardCorners(image, (9,6), corners2, ret)
            cv2.imwrite("static/photos/out.png", image)

    else:
        raise Exception("No image detected. Please! try again")
