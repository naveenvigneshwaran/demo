from pysimverse import Drone
import time
import cv2


drone = Drone()
drone.connect()

drone.streamon()
drone.take_off()

while True:
    frame, is_success = drone.get_frame()
    cv2.imshow("Drone Camera", frame)
    cv2.waitKey(1)
def main():
    drone = Drone()
    drone.connect()
    drone.take_off()
    

    while True:
        if keyboard.is_pressed('q'):
            drone.land()
            break
        elif keyboard.is_pressed('w'):
            drone.move_forward(SPEED)
        elif keyboard.is_pressed('s'):
            drone.move_backward(SPEED)
        elif keyboard.is_pressed('a'):
            drone.move_left(SPEED)
        elif keyboard.is_pressed('d'):
            drone.move_right(SPEED)
        else:
            drone.hover()
        time.sleep(0.1)
def main():
    up_down = SPEED if keyboard.is_pressed("up") else -SPEED if keyboard.is_pressed("down") else 0
    if keyboard.is_pressed("down"):
        up_down = -SPEED
    yaw = ROTATE_SPEED if keyboard.is_pressed("d") else -ROTATE_SPEED if keyboard.is_pressed("right") else 0
    time.sleep(0.05)
    
drone.land()
time.sleep(1)
