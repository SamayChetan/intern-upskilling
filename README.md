# Face Mask Detection API

A computer vision project that detects whether people are wearing face masks using a YOLOv8 model exported to ONNX. The application exposes a FastAPI endpoint for inference, publishes detection results over MQTT, and can be deployed using Docker.

---

## Features

- YOLOv8 face mask detection
- ONNX Runtime inference
- FastAPI REST API
- MQTT integration for publishing detections
- Docker support
- Model benchmarking and optimization

---

## Project Structure

```
.
├── app.py
├── benchmark_onnx.py
├── benchmark_latency.py
├── export_onnx.py
├── quantize_model.py
├── onnx_inference.py
├── publisher.py
├── subscriber.py
├── train_yolo.py
├── configs/
├── datasets/
├── runs/
├── README.md
├── OPTIMIZATION.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd internship-task
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Running the FastAPI Server

Start the API:

```bash
uvicorn app:app --reload
```

Open:

```
http://localhost:8000/docs
```

Upload an image using the `/predict` endpoint.

---

## MQTT

Run the subscriber:

```bash
python subscriber.py
```

The FastAPI application automatically publishes prediction results to the configured MQTT topic after every inference.

---

## Docker

Build the image:

```bash
docker build -t face-mask-api .
```

Run the container:

```bash
docker run -p 8000:8000 face-mask-api
```

Open:

```
http://localhost:8000/docs
```

---

## Model Optimization

The project includes:

- ONNX export
- Dynamic quantization
- Latency benchmarking
- Performance comparison

See `OPTIMIZATION.md` for detailed benchmark results.

---

## Technologies Used

- Python
- YOLOv8 (Ultralytics)
- ONNX Runtime
- FastAPI
- MQTT (Paho MQTT)
- Docker
- OpenCV

---

## Future Improvements

- Move deployed models into a dedicated `models/` directory.
- Add confidence threshold configuration.
- Support batch inference.
- Add object tracking (ByteTrack).

## Architecture

Input Video
     │
     ▼
OpenCV
     │
     ▼
YOLOv8 Detector
     │
     ▼
Confidence Threshold Check
     │
     ▼
JSON Payload Builder
     │
     ▼
MQTT Publisher
     │
     ▼
MQTT Subscriber

## Responsible AI

This project includes confidence-based uncertainty flagging to improve the reliability of predictions.

When the model produces detections with confidence below 0.5, the application marks the frame as **uncertain** instead of presenting the prediction as completely reliable. This follows the principle of communicating uncertainty rather than making overconfident decisions.

For assistive technologies such as MITRA, this is especially important because users may rely on the system's output in real time. Incorrect but confident predictions can negatively affect user safety. Flagging uncertain predictions allows downstream systems or users to take additional precautions when necessary.