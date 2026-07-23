import json
import cv2
import paho.mqtt.client as mqtt

from ultralytics import YOLO
from utils import build_payload

# Load YOLO model
model = YOLO("runs/detect/train-3/weights/best.pt")

# Open video
cap = cv2.VideoCapture("assets/test_video.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("Video opened successfully!")

frame_id = 0

# MQTT Configuration
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "samay/module3/demo"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)

while True:
    success, frame = cap.read()

    if not success:
        print("End of video.")
        break

    frame_id += 1

    # Run YOLO detection
    results = model(frame, verbose=False)

    detections = []
    low_conf_count = 0

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = results[0].names[class_id]

        detections.append({
            "class": class_name,
            "confidence": round(confidence, 2)
        })

        if confidence < 0.5:
            low_conf_count += 1

    uncertain = low_conf_count > 0

    # Build JSON payload
    output = build_payload(
        frame_id,
        detections,
        uncertain,
        low_conf_count
    )

    # Publish to MQTT
    payload = json.dumps(output)
    result = client.publish(TOPIC, payload)

    # Print for debugging
    print(json.dumps(output, indent=4))
    print("Publish result:", result.rc)

    # Draw detections
    annotated_frame = results[0].plot()

    # Show video
    cv2.imshow("Face Mask Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
client.disconnect()