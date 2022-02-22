import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 3840)
cam.set(4, 2160)
cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)

    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
