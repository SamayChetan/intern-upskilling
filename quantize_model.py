import os
import torch
from ultralytics import YOLO

# Load the trained YOLO model
yolo = YOLO("runs/detect/train-3/weights/best.pt")

# Extract the underlying PyTorch model
model = yolo.model
model.eval()

# Apply dynamic quantization
quantized_model = torch.quantization.quantize_dynamic(
    model,
    {torch.nn.Linear},
    dtype=torch.qint8
)

# Save the quantized model
torch.save(
    quantized_model.state_dict(),
    "runs/detect/train-3/weights/best_quantized.pt"
)

# Compare file sizes
original_size = os.path.getsize(
    "runs/detect/train-3/weights/best.pt"
) / (1024 * 1024)

quantized_size = os.path.getsize(
    "runs/detect/train-3/weights/best_quantized.pt"
) / (1024 * 1024)

print(f"Original model size : {original_size:.2f} MB")
print(f"Quantized model size: {quantized_size:.2f} MB")