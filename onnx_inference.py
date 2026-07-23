import onnxruntime as ort
import cv2
import numpy as np

# Load ONNX model
session = ort.InferenceSession(
    "runs/detect/train-3/weights/best.onnx",
    providers=["CPUExecutionProvider"]
)

# Get model input details
input_name = session.get_inputs()[0].name
input_shape = session.get_inputs()[0].shape

print("Model loaded successfully!")
print("Input name:", input_name)
print("Input shape:", input_shape)

# Read one test image
image_path = "datasets/face_mask/archive/dataset/images/test/nouveau-virus-en-chine-la-ville-de-wuhan-mise-en-quarantaine-1.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Could not read image: {image_path}")

# Resize to model input size
image = cv2.resize(image, (640, 640))

# Convert BGR → RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Normalize
image = image.astype(np.float32) / 255.0

# Change HWC → CHW
image = np.transpose(image, (2, 0, 1))

# Add batch dimension
image = np.expand_dims(image, axis=0)

# Run inference
outputs = session.run(None, {input_name: image})

print("Inference successful!")
print("Output shape:", outputs[0].shape)