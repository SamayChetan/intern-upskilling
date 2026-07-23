from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("runs/detect/train-3/weights/best.pt")

# Open video
cap = cv2.VideoCapture("assets/test_video.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("Video opened successfully!")

while True:
    success, frame = cap.read()

    if not success:
        print("End of video.")
        break

    # Run YOLO detection
    results = model(frame, verbose=False)

    # Draw detections on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("Face Mask Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()