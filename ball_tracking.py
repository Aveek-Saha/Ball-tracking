import numpy as np
import cv2
import serial
import time

ser=serial.Serial('COM4',9600)#initialises the port connected to the arduino

import imutils

# define the lower and upper boundaries of the "orange"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (0,50,214)
greenUpper = (103,255,255)


camera = cv2.VideoCapture(1)

while True:
        (grabbed, frame) = camera.read()

        frame = imutils.resize(frame, width=600)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

# find contours in the mask and initialize the current
# (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

# only proceed if at least one contour was found
        if len(cnts) > 0:
# find the largest contour in the mask, then use
# it to compute the minimum enclosing circle and
# centroid
                ser.write('Y{0:d}'.format(1))
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
# only proceed if the radius meets a minimum size
                if radius > 10:
# draw the circle and centroid on the frame,
                        ser.write('Z{0:d}'.format(int(radius)))
                        cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)

        else:
                ser.write('Y{0:d}'.format(0))
# show the frame to our screen
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(5) & 0xFF

# if the 'q' key is pressed, stop the loop
        if key == 27:
                break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
