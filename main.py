import glob
from ultralytics import YOLO

from agents.perception_agent import PerceptionAgent
from agents.reasoning_agent import ReasoningAgent
from agents.planning_agent import PlanningAgent
from agents.advisory_agent import AdvisoryAgent


def run_pipeline(image_path):
    print("Starting Agentic AI Pipeline...\n")

    # -----------------------------
    # 1. Load YOLOv8 Disease Model
    # -----------------------------
    #model = YOLO("runs/detect/train5/weights/best.pt")
    def load_latest_yolo_model():
        weight_files = glob.glob("runs/detect/train*/weights/best.pt")
        if not weight_files:
            raise FileNotFoundError("No trained YOLO model found.")
        latest_model = sorted(weight_files)[-1]
        return YOLO(latest_model)


    # inside run_pipeline()
    model = load_latest_yolo_model()

    print("Running disease detection...")
    results = model(image_path, conf=0.1)

    # Default values
    detected_disease = "healthy"
    confidence_score = 0.0

    # Read YOLO output
    for r in results:
        if r.boxes is not None and len(r.boxes) > 0:
            box = r.boxes[0]
            detected_disease = model.names[int(box.cls[0])]
            confidence_score = float(box.conf[0])

    print(f"Disease Detected: {detected_disease}")
    print(f"Confidence Score: {confidence_score:.2f}\n")

    # -----------------------------
    # 2. Perception Agent
    # -----------------------------
    perception_agent = PerceptionAgent()
    disease_info = perception_agent.process_disease_output(
        detected_disease,
        confidence_score
    )

    perception_state = perception_agent.get_perception_state(disease_info)

    print("Perception State:")
    print(perception_state, "\n")

    # -----------------------------
    # 3. Reasoning Agent
    # -----------------------------
    reasoning_agent = ReasoningAgent()
    issues = reasoning_agent.analyze_crop_health(perception_state)

    print("Identified Issues:")
    for issue in issues:
        print("-", issue)
    print()

    # -----------------------------
    # 4. Planning Agent
    # -----------------------------
    planning_agent = PlanningAgent()
    actions = planning_agent.generate_action_plan(issues)

    print("Action Plan:")
    for action in actions:
        print(action)
    print()

    # -----------------------------
    # 5. Advisory Agent
    # -----------------------------
    advisory_agent = AdvisoryAgent()
    advisories = advisory_agent.generate_advisory(actions)

    print("Final Farmer Advisory:")
    for advice in advisories:
        print(advice)

    print("\nPipeline execution completed.")


if __name__ == "__main__":
    test_image = "data/plant_images/valid/images/img058.JPG"  # change if needed
    run_pipeline(test_image)
