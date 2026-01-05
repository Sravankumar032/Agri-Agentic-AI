import sys
import os
import glob
from PIL import Image


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from ultralytics import YOLO

from agents.perception_agent import PerceptionAgent
from agents.reasoning_agent import ReasoningAgent
from agents.planning_agent import PlanningAgent
from agents.advisory_agent import AdvisoryAgent


# Load model once
@st.cache_resource
def load_model():
    weight_files = glob.glob("runs/detect/train*/weights/best.pt")
    latest_model = sorted(weight_files)[-1]
    return YOLO(latest_model)


def run_agentic_pipeline(image):
    model = load_model()

    # YOLO inference
    #results = model(image, conf=0.1)
    pil_image = Image.open(image).convert("RGB")
    results = model(pil_image, conf=0.1)

    detected_disease = "healthy"
    confidence_score = 0.0

    for r in results:
        if r.boxes is not None and len(r.boxes) > 0:
            box = r.boxes[0]
            detected_disease = model.names[int(box.cls[0])]
            confidence_score = float(box.conf[0])

    # Agents
    perception_agent = PerceptionAgent()
    reasoning_agent = ReasoningAgent()
    planning_agent = PlanningAgent()
    advisory_agent = AdvisoryAgent()

    disease_info = perception_agent.process_disease_output(
        detected_disease, confidence_score
    )

    perception_state = perception_agent.get_perception_state(disease_info)
    issues = reasoning_agent.analyze_crop_health(perception_state)
    actions = planning_agent.generate_action_plan(issues)
    advisories = advisory_agent.generate_advisory(actions)

    return detected_disease, confidence_score, issues, advisories


# ---------------- UI ---------------- #

st.set_page_config(page_title="Agentic AI for Precision Farming", layout="centered")

st.title("🌱 Agentic AI System for Autonomous Precision Farming")
st.write("Upload a crop leaf image to receive automated advisory.")

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Run Advisory"):
        with st.spinner("Analyzing crop health..."):
            disease, confidence, issues, advisories = run_agentic_pipeline(uploaded_file)

        st.subheader("🔍 Detection Result")
        st.write(f"**Disease Detected:** {disease}")
        st.write(f"**Confidence:** {confidence:.2f}")

        st.subheader("🧠 Identified Issues")
        for issue in issues:
            st.write(f"- {issue}")

        st.subheader("📋 Farmer Advisory")
        for advice in advisories:
            st.success(advice["advisory_message"])
            st.write(f"**Priority:** {advice['priority']}")
            st.write(f"**Recommended Time:** {advice['recommended_time']}")