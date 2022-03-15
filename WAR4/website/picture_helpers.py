# program to capture single image from webcam in python
# SOURCE : https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
import cv2

def take_pic():
    # initialize the camera
    # If you have multiple camera connected with
    # current device, assign a value in cam_port
    # variable according to that
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:

        # showing result, it take frame name and image
        # output
        cv2.imshow("xyz1", image)

        # saving image in local storage
        cv2.imwrite("static/photos/out.png", image)

        # If keyboard interrupt occurs, destroy image
        # window
        #cv2.waitKey(0)
        #cv2.destroyWindow("xyz")

    # If captured image is corrupted, moving to else part
    else:
        raise Exception("No image detected. Please! try again")
