import cv2
import time

print(cv2.getBuildInformation())

time_sum = 0
frames = 0

capture = cv2.VideoCapture()
capture.open(0 + cv2.CAP_DSHOW)

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
capture.set(cv2.CAP_PROP_FOURCC, fourcc)
capture.set(cv2.CAP_PROP_FPS, 60)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

while(1):
    before_timer = time.perf_counter()
    ret, frame = capture.read()
    if frame is None:
        print("Frame is empty")
        break
    else:
        cv2.imshow('VIDEO', frame)
        after_timer = time.perf_counter() - before_timer
        time_sum += after_timer
        frames += 1
        if frames % 30 == 0:
            print("{} per second".format(frames/time_sum))
        cv2.waitKey(1)
