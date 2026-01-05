from perception_agent import PerceptionAgent
from reasoning_agent import ReasoningAgent
from planning_agent import PlanningAgent
from advisory_agent import AdvisoryAgent

# Initialize agents
perception_agent = PerceptionAgent()
reasoning_agent = ReasoningAgent()
planning_agent = PlanningAgent()
advisory_agent = AdvisoryAgent()

# Simulated disease detection
disease_info = perception_agent.process_disease_output(
    disease_label="leaf_blight",
    confidence=0.85
)

perception_state = perception_agent.get_perception_state(disease_info)
issues = reasoning_agent.analyze_crop_health(perception_state)
actions = planning_agent.generate_action_plan(issues)
advisories = advisory_agent.generate_advisory(actions)

print("Farmer Advisory:")
for advice in advisories:
    print(advice)