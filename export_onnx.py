from ultralytics import YOLO

model = YOLO("runs/detect/train-3/weights/best.pt")

model.export(
    format="onnx",
    imgsz=640
)