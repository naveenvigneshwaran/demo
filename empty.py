from pysimverse import Drone

from cvzone.ColorModule import ColorFinder

import cv2

import cvzone

import time



# Connect to drone

drone = Drone()

drone.connect()

drone.streamon()
drone.take_off(takeoff_height=25)



# Color detection setup

myColorFinder = ColorFinder(trackBar=True)

hsvVals = {'hmin': 0, 'smin': 113, 'vmin': 73, 'hmax': 10, 'smax': 229, 'vmax': 255}



# Bang-bang settings

deadband_px = 2       # How close to center before going straight

yaw_power = 0.4         # How hard to turn



while True:



    frame, ok = drone.get_frame()

    if not ok:

        continue



    # Detect line

    imgLine, mask = myColorFinder.update(frame, hsvVals)

    imgContours, conFound = cvzone.findContours(frame, mask)



    yaw = 0      # Default = go straight



    # If contour found, compute error

    if conFound:

        center_x = frame.shape[1] // 2

        cx = conFound[0]['center'][0]

        error = center_x - cx



        # Bang-Bang Logic

        if abs(error) < deadband_px:

            yaw = 0                    # centered → straight

        elif error < 0:

            yaw = +yaw_power           # line is LEFT → turn RIGHT

        else:

            yaw = -yaw_power           # line is RIGHT → turn LEFT



    # Send simple control

    drone.send_rc_control(0, 20, 0, yaw)



    # Display

    imgStack = cvzone.stackImages([frame, imgLine, mask, imgContours], 2, 0.6)

    cv2.imshow("Image Stack", imgStack)



    if cv2.waitKey(1) & 0xFF == ord('q'):

        break