import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width, height)
#cv2.destroyAllWindows()
