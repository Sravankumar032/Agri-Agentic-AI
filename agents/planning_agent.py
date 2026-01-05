class PlanningAgent:
    def __init__(self):
        pass

    def generate_action_plan(self, issues):
        """
        Converts identified issues into agronomic action plans
        """

        actions = []

        for issue in issues:
            if "Severe crop disease" in issue:
                actions.append({
                    "action": "Apply fungicide",
                    "priority": "High",
                    "timeframe": "Within 48 hours"
                })

            elif "Moderate crop disease" in issue:
                actions.append({
                    "action": "Monitor disease progression and apply preventive spray",
                    "priority": "Medium",
                    "timeframe": "Within 5 days"
                })

            elif "Mild crop disease" in issue:
                actions.append({
                    "action": "Regular monitoring",
                    "priority": "Low",
                    "timeframe": "Next 7 days"
                })

            elif "Crop under vegetation stress" in issue:
                actions.append({
                    "action": "Adjust irrigation schedule",
                    "priority": "Medium",
                    "timeframe": "Immediate"
                })

            elif "High weather-related risk" in issue:
                actions.append({
                    "action": "Delay irrigation and protect crop",
                    "priority": "High",
                    "timeframe": "As per weather forecast"
                })

        if not actions:
            actions.append({
                "action": "No immediate action required",
                "priority": "Low",
                "timeframe": "Routine monitoring"
            })

        return actions