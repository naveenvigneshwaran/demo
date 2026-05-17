import cv2
import numpy as np

# Allowed QR data
ALLOWED_QR = "http://bn.m.wikipedia.org"

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# QR detector
qr_detector = cv2.QRCodeDetector()

# Real QR width in cm
REAL_QR_WIDTH = 5.0

# Approximate focal length
FOCAL_LENGTH = 700

while True:

    success, frame = cap.read()

    if not success:
        print("Camera not working")
        break

    # Detect QR
    data, bbox, _ = qr_detector.detectAndDecode(frame)

    if bbox is not None and data:

        bbox = bbox.astype(int)

        # Draw QR boundary
        for i in range(len(bbox[0])):

            pt1 = tuple(bbox[0][i])
            pt2 = tuple(bbox[0][(i + 1) % len(bbox[0])])

            cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

        # Calculate QR width in pixels
        x1, y1 = bbox[0][0]
        x2, y2 = bbox[0][1]

        qr_width_pixels = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # Estimate distance
        distance = (REAL_QR_WIDTH * FOCAL_LENGTH) / qr_width_pixels

        # Accuracy estimation
        accuracy = min(100, int((qr_width_pixels / 200) * 100))

        # Check allowed QR
        if data == ALLOWED_QR:

            status = "ACCESS ALLOWED"
            color = (0, 255, 0)

        else:

            status = "ACCESS DENIED"
            color = (0, 0, 255)

        # Show QR data
        cv2.putText(
            frame,
            f"QR: {data}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

        # Show status
        cv2.putText(
            frame,
            status,
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            3
        )

        # Show distance
        cv2.putText(
            frame,
            f"Distance: {distance:.2f} cm",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

        # Show accuracy
        cv2.putText(
            frame,
            f"Accuracy: {accuracy}%",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

    # Display video
    cv2.imshow("Vending QR Access System", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release
cap.release()
cv2.destroyAllWindows()