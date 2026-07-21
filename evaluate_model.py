from ultralytics import YOLO

# Load the trained model
model = YOLO("runs/detect/train-3/weights/best.pt")

# Evaluate on the validation set
metrics = model.val(
    data="configs/face_mask.yaml",
    split="test"
)

print("\n===== Validation Results =====")
print(f"mAP@0.5: {metrics.box.map50:.4f}")
print(f"mAP@0.5:0.95: {metrics.box.map:.4f}")
print(f"Precision: {metrics.box.mp:.4f}")
print(f"Recall: {metrics.box.mr:.4f}")