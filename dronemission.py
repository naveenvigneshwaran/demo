import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options =python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

image = mp.Image.create_from_file("vending QR1.png")

detection_result = detector.detect(image)

annotated_image =draw_landmarks_on_image(image,numpy_view(), detection_result)
cv2_imshow(cv2.cvColor(annotated_image, cv2.COLOR_RGB2BGR))