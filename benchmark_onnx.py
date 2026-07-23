import os
import time
import statistics
import cv2
import numpy as np
import onnxruntime as ort

image_folder = "datasets/face_mask/archive/dataset/images/test"

# Load ONNX model
session = ort.InferenceSession(
    "runs/detect/train-3/weights/best.onnx",
    providers=["CPUExecutionProvider"]
)

input_name = session.get_inputs()[0].name

# Get image paths
image_paths = [
    os.path.join(image_folder, f)
    for f in os.listdir(image_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

# Repeat images until we have 100
while len(image_paths) < 100:
    image_paths.extend(image_paths)

image_paths = image_paths[:100]

print(f"Found {len(image_paths)} images")

# Warm-up (5 runs)
print("Warming up...")
for path in image_paths[:5]:
    img = cv2.imread(path)
    img = cv2.resize(img, (640, 640))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)

    session.run(None, {input_name: img})

print("Measuring inference latency...")

times = []

for path in image_paths:
    img = cv2.imread(path)
    img = cv2.resize(img, (640, 640))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)

    start = time.perf_counter()
    session.run(None, {input_name: img})
    end = time.perf_counter()

    times.append((end - start) * 1000)

mean_latency = statistics.mean(times)
std_latency = statistics.stdev(times)
fps = 1000 / mean_latency

print("\n===== ONNX Benchmark =====")
print(f"Images: {len(image_paths)}")
print(f"Mean latency: {mean_latency:.2f} ms")
print(f"Std latency : {std_latency:.2f} ms")
print(f"FPS: {fps:.2f}")