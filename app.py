from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import tempfile
import os
import json
import paho.mqtt.client as mqtt

app = FastAPI()

# Load ONNX model
model = YOLO("runs/detect/train-3/weights/best.onnx")

# MQTT Configuration
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "samay/module3/demo"

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.connect(BROKER, PORT, 60)
mqtt_client.loop_start()


@app.get("/")
def home():
    return {"message": "YOLO ONNX API is running!"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Check if uploaded file is an image
    if not file.content_type.startswith("image/"):
        return {
            "error": "Uploaded file is not an image."
        }

    # Save uploaded image temporarily
    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(await file.read())
        temp_path = temp.name

    # Run YOLO inference
    results = model.predict(temp_path)

    detections = []

    for box in results[0].boxes:
        detections.append({
            "class": model.names[int(box.cls)],
            "confidence": float(box.conf),
            "bbox": box.xyxy.tolist()[0]
        })

    # Delete temporary image
    os.remove(temp_path)

    # No detections found
    if len(detections) == 0:
        mqtt_client.publish(
            TOPIC,
            json.dumps({
                "message": "No detections found",
                "detections": []
            })
        )

        return {
            "message": "No detections found.",
            "detections": []
        }

    # Publish detections to MQTT
    mqtt_client.publish(
        TOPIC,
        json.dumps(detections)
    )

    return {
        "detections": detections
    }