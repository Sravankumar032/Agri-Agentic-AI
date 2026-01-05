from perception_agent import PerceptionAgent

# Simulated YOLO output
detected_disease = "leaf_blight"
confidence_score = 0.78

agent = PerceptionAgent()

disease_info = agent.process_disease_output(
    detected_disease,
    confidence_score
)

perception_state = agent.get_perception_state(disease_info)

print("Perception State:")
print(perception_state)
