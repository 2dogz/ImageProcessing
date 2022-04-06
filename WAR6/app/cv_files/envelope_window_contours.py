import cv2


# bubble sort the objects so we get the smaller area items first
# smaller area item should be the the ArUcu marker
# source : https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubble_sort(arr, n):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if cv2.contourArea(arr[j]) > cv2.contourArea(arr[j + 1]) :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# function to detect objects in frame and draw contours, returns array
def detect_objects(frame):
    # convert to grayscale
    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect envelope edges
    mask = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 6)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # write contours to array
    objects_contours = []
    for each in contours:
        area = cv2.contourArea(each)
        # exclude objects under with area under 2000 pixels
        if area > 2000:
            objects_contours.append(each)

    # sort array - ascending order
    arr = bubble_sort(objects_contours, len(objects_contours))

    # return array of contours in ascending order
    return arr


# read in image
img = cv2.imread("static/photos/blue_img.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert the image to grayscale format
#img_gray = cv2.Canny(img_gray, 25, 50 )
cv2.imshow('gray image', img_gray)
cv2.waitKey(0)

# # call detect_objects function
contours2 = detect_objects(img_gray)
cv2.drawContours(img, contours2, -1, (0, 255, 0), 3)
cv2.imshow("Image", img)
cv2.waitKey(0)

# apply binary thresholding
# ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# # visualize the binary image
# cv2.imshow('Binary image', thresh)
# cv2.waitKey(0)
# cv2.imwrite('image_thres1.jpg', thresh)
# cv2.destroyAllWindows()
