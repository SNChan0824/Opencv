# Save this file as OpenCV-2-video.py

#import library
import cv2

# Capture a video file
capture = cv2.VideoCapture('Resources/SPIDER-MAN - Trailer.mp4')

# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()

    # below line is to resize video image frame, uncomment if you want to resize
    img = cv2.resize(img, (int(img.shape[1] / 1.5), int(img.shape[0] / 1.5)))

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()