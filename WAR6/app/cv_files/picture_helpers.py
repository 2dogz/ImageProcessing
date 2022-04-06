# program to capture single image from webcam in python
# SOURCE : https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
import cv2

def take_pic():

    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    cam.set(3, 1920)
    cam.set(4, 1080)
    width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(width, height)

    result, image = cam.read()
    if result:
        cv2.imwrite("static/photos/input.png", image)
        cv2.imwrite("static/photos/out.png", image)
    else:
        print("No image detected. Please! try again")
