class AdvisoryAgent:
    def __init__(self):
        pass

    def generate_advisory(self, action_plan):
        """
        Converts action plans into farmer-friendly advisories
        """

        advisories = []

        for action in action_plan:
            message = ""

            if action["action"] == "Apply fungicide":
                message = (
                    "Disease has been detected in your crop. "
                    "It is advised to apply a recommended fungicide within the next two days "
                    "to prevent further spread."
                )

            elif "preventive" in action["action"]:
                message = (
                    "Early signs of disease are observed. "
                    "Please monitor the crop closely and apply a preventive spray if symptoms increase."
                )

            elif "Regular monitoring" in action["action"]:
                message = (
                    "Minor disease symptoms detected. "
                    "No immediate treatment is required, but continue regular field observation."
                )

            elif "Adjust irrigation" in action["action"]:
                message = (
                    "Vegetation stress is observed. "
                    "Please adjust irrigation timing and ensure adequate soil moisture."
                )

            elif "No immediate action" in action["action"]:
                message = (
                    "Your crop condition appears normal. "
                    "Continue routine monitoring and follow standard farming practices."
                )

            advisories.append({
                "advisory_message": message,
                "priority": action["priority"],
                "recommended_time": action["timeframe"]
            })

        return advisories