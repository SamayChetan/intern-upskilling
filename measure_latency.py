from ultralytics import YOLO
import time
import os
import glob

# Load trained model
model = YOLO("runs/detect/train-2/weights/best.pt")

# Path to test images
image_folder = "datasets/face_mask/archive/dataset/images/test"

# Get all image files
image_paths = []
for ext in ["*.jpg", "*.jpeg", "*.png"]:
    image_paths.extend(glob.glob(os.path.join(image_folder, ext)))

# Use at most 100 images
image_paths = image_paths[:100]

print(f"Found {len(image_paths)} images")

# Warm-up (5 dummy inferences)
print("Warming up...")
for _ in range(5):
    model.predict(image_paths[0], verbose=False)

# Measure inference time
print("Measuring inference latency...")

start = time.perf_counter()

for image in image_paths:
    model.predict(image, verbose=False)

end = time.perf_counter()

total_time = end - start
avg_time = total_time / len(image_paths)
fps = len(image_paths) / total_time

print(f"\nTotal images: {len(image_paths)}")
print(f"Total time: {total_time:.2f} seconds")
print(f"Average latency: {avg_time*1000:.2f} ms/image")
print(f"FPS: {fps:.2f}")