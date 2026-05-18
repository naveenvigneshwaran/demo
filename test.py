import numpy as np
import cv2
from pathlib import Path


def safe_destroy_windows():
    try:
        cv2.destroyAllWindows()
    except cv2.error as error:
        print(f"OpenCV GUI backend unavailable: {error}")


project_dir = Path(__file__).resolve().parent
fallback_video = project_dir / "video.mp4"

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to open camera 0.")
    camera.release()

    if fallback_video.exists():
        print(f"Falling back to video file: {fallback_video.name}")
        camera = cv2.VideoCapture(str(fallback_video))
    else:
        camera = None

if camera is None or not camera.isOpened():
    print("No camera or fallback video source is available.")
else:
    print("The camera is successfully opened")

    while True:
        success, frame = camera.read()
        if not success:
            print("Not able to read the frame. End.")
            break

        frame2 = cv2.GaussianBlur(frame, (31, 31), 0)
        combined = np.hstack((frame, frame2))
        try:
            cv2.imshow("Camera video", combined)
        except cv2.error as error:
            print(f"OpenCV GUI backend unavailable: {error}")
            break

        if cv2.waitKey(1) & 0xFF == ord("c"):
            break

camera.release()
safe_destroy_windows()
    
