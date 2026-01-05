class PerceptionAgent:
    def __init__(self):
        pass

    def process_disease_output(self, disease_label, confidence):
        """
        Converts disease detection output into structured perception
        """
        if confidence >= 0.6:
            severity = "high"
        elif confidence >= 0.3:
            severity = "medium"
        else:
            severity = "low"

        return {
            "disease": disease_label,
            "confidence": round(confidence, 2),
            "severity": severity
        }

    def get_perception_state(self, disease_result, ndvi=None, weather=None):
        """
        Aggregates all perception signals into a unified state
        """
        state = {
            "crop_health": disease_result,
            "ndvi": ndvi if ndvi else "not_available",
            "weather": weather if weather else "not_available"
        }
        return state