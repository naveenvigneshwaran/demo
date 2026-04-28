from pathlib import Path

import cv2
from ultralytics import YOLO


def safe_destroy_windows():
    try:
        cv2.destroyAllWindows()
    except cv2.error as error:
        print(f"OpenCV GUI backend unavailable: {error}")


project_dir = Path(__file__).resolve().parent
model_path = project_dir / "yolov8n.pt"
video_path = project_dir / "video.mp4"

if not model_path.exists():
    raise FileNotFoundError(f"Model not found: {model_path}")

if not video_path.exists():
    raise FileNotFoundError(f"Video not found: {video_path}")

model = YOLO(str(model_path))
cap = cv2.VideoCapture(str(video_path))

if not cap.isOpened():
    raise RuntimeError(f"Unable to open video: {video_path}")

while True:
    success, frame = cap.read()
    if not success:
        print("End of video.")
        break

    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    try:
        cv2.imshow("YOLO Demo", annotated_frame)
    except cv2.error as error:
        print(f"OpenCV GUI backend unavailable: {error}")
        break

    if cv2.waitKey(1) & 0xFF == ord("c"):
        break

cap.release()
safe_destroy_windows()
