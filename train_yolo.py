from ultralytics import YOLO
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Train YOLOv8 on Face Mask Dataset")

parser.add_argument(
    "--data",
    type=str,
    default="configs/face_mask.yaml",
    help="Path to dataset YAML file"
)

parser.add_argument(
    "--epochs",
    type=int,
    default=50,
    help="Number of training epochs"
)

args = parser.parse_args()

# Load pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data=args.data,
    epochs=args.epochs,
    imgsz=640,
    batch=4,
    device="cpu",
    seed=42
)