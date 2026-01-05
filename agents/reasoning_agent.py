class ReasoningAgent:
    def __init__(self):
        pass

    def analyze_crop_health(self, perception_state):
        """
        Applies reasoning logic on perception state
        to identify agronomic issues.
        """

        issues = []

        crop_health = perception_state.get("crop_health", {})
        disease = crop_health.get("disease")
        severity = crop_health.get("severity")

        # Disease-based reasoning
        if disease != "healthy":
            if severity == "high":
                issues.append("Severe crop disease detected")
            elif severity == "medium":
                issues.append("Moderate crop disease detected")
            else:
                issues.append("Mild crop disease detected")

        # NDVI-based reasoning (placeholder)
        ndvi = perception_state.get("ndvi")
        if isinstance(ndvi, (int, float)):
            if ndvi < 0.4:
                issues.append("Crop under vegetation stress")
            elif ndvi < 0.6:
                issues.append("Moderate vegetation health")

        # Weather-based reasoning (placeholder)
        weather = perception_state.get("weather")
        if isinstance(weather, dict):
            if weather.get("risk") == "high":
                issues.append("High weather-related risk identified")

        if not issues:
            issues.append("Crop health appears normal")

        return issues