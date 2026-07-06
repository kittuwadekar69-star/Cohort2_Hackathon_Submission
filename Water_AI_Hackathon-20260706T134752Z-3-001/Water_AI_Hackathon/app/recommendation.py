def generate_recommendations(
    scarcity,
    groundwater,
    rainfall,
    agriculture,
    consumption
):

    recommendations = []

    if scarcity.lower() == "high":
        recommendations.append("🚨 High water scarcity detected.")

    if groundwater > 60:
        recommendations.append(
            "Increase groundwater recharge initiatives."
        )

    if rainfall < 500:
        recommendations.append(
            "Promote rainwater harvesting."
        )

    if agriculture > 70:
        recommendations.append(
            "Adopt drip irrigation techniques."
        )

    if consumption > 300:
        recommendations.append(
            "Reduce unnecessary water consumption."
        )

    if not recommendations:
        recommendations.append(
            "Water resources are currently stable."
        )

    return recommendations