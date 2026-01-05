from ultralytics import YOLO

# Load lightweight YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train on your dataset
model.train(
    data=r"C:\Users\DELL\OneDrive\Documents\GitHub\Agri-Agentic-AI\data\plant_images/data.yaml",
    epochs=20,          # keep small for CPU
    imgsz=416,          # safe image size
    batch=4,            # safe for 4GB RAM
    device="cpu"
)