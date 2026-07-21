from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="configs/face_mask.yaml",
    epochs=50,
    imgsz=640,
    batch=4,
    device="cpu",
    seed=42
)