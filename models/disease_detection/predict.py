import glob
from ultralytics import YOLO

#model = YOLO("runs/detect/train5/weights/best.pt")
def load_latest_yolo_model():
    weight_files = glob.glob("runs/detect/train*/weights/best.pt")
    if not weight_files:
        raise FileNotFoundError("No trained YOLO model found.")
    latest_model = sorted(weight_files)[-1]
    return YOLO(latest_model)


model = load_latest_yolo_model()


# Test image path
image_path = "data/plant_images/valid/images/img021.JPG"

results = model(image_path, conf=0.4)

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls]

        print(f"Disease Detected: {label}")
        print(f"Confidence: {conf:.2f}")
