# Save this file as OpenCV-1-Read.py
import cv2

# read the image Lena.png and save into img
img = cv2.imread('Resources/Spider_Man_Tom_Holland.jpg')

# Show the resized image and grayscale image onto two windows
cv2.imshow('Tom',img)

# wait for any key input to terminate the program
cv2.waitKey(0)
