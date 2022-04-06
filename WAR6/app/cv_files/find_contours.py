import cv2


def contoursPicture():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    # set resolution
    cam.set(3, 1920)
    cam.set(4, 1080)

    # print resolutions - debug
    width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(width, height)

    result, image = cam.read()
    if result:
        cv2.imwrite("static/photos/input.png", image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
        cv2.imwrite("static/photos/out.png", image)
    else:
        raise Exception("No image detected. Please! try again")
