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
fallback_video = project_dir / "video.mp4"

if not model_path.exists():
    raise FileNotFoundError(f"Model not found: {model_path}")

model = YOLO(str(model_path))
cap = cv2.VideoCapture(0)
source_name = "camera 0"

if not cap.isOpened():
    print("Unable to open camera 0.")
    cap.release()

    if fallback_video.exists():
        print(f"Falling back to video file: {fallback_video.name}")
        cap = cv2.VideoCapture(str(fallback_video))
        source_name = fallback_video.name

if not cap.isOpened():
    raise RuntimeError("No camera or fallback video source is available.")

print(f"Running object detection on {source_name}. Press 'c' to close.")

while True:
    success, frame = cap.read()
    if not success:
        print("End of source.")
        break

    results = model.predict(frame, verbose=False)
    annotated_frame = results[0].plot()

    try:
        cv2.imshow("YOLO Object Detection", annotated_frame)
    except cv2.error as error:
        print(f"OpenCV GUI backend unavailable: {error}")
        break

    if cv2.waitKey(1) & 0xFF == ord("c"):
        break

cap.release()
safe_destroy_windows()
