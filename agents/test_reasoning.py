from perception_agent import PerceptionAgent
from reasoning_agent import ReasoningAgent

# Simulated perception output
perception_agent = PerceptionAgent()
reasoning_agent = ReasoningAgent()

disease_info = perception_agent.process_disease_output(
    disease_label="leaf_blight",
    confidence=0.78
)

perception_state = perception_agent.get_perception_state(
    disease_result=disease_info
)

issues = reasoning_agent.analyze_crop_health(perception_state)

print("Identified Issues:")
for issue in issues:
    print("-", issue)
