import random
from pydantic import BaseModel

class PolymerProperties(BaseModel):
    """Class representing polymer properties."""
    glass_transition_temp: float
    mechanical_strength: float
    thermal_stability: float

def mock_polymer_prediction(structure: str, additives: list[str], temperature: float) -> PolymerProperties:
    """
    Mock function to simulate polymer property predictions based on input parameters.

    Args:
        structure (str): The chemical structure or identifier of the polymer.
        additives (list[str]): List of additives used in the polymer.
        temperature (float): The temperature for which properties are being predicted.

    Returns:
        PolymerProperties: Predicted polymer properties.
    """
    # Simulate some random behavior based on input values to mimic a real model
    base_temp_adjustment = (len(additives) * 0.1) + (temperature * 0.01)
    strength_factor = 1 + len(structure) * 0.02
    
    glass_transition_temp = random.uniform(100, 500) * (1 + base_temp_adjustment / 100)
    mechanical_strength = random.uniform(50, 300) * strength_factor
    thermal_stability = random.uniform(200, 600) * (1 + base_temp_adjustment / 200)

    return PolymerProperties(
        glass_transition_temp=round(glass_transition_temp, 2),
        mechanical_strength=round(mechanical_strength, 2),
        thermal_stability=round(thermal_stability, 2)
    )
