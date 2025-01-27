from pydantic import BaseModel
from typing import List, Optional
import random

# Define schemas
class PolymerInput(BaseModel):
    structure: str
    additives: List[str]
    temperature: float

class PolymerProperties(BaseModel):
    glass_transition_temp: float
    mechanical_strength: float
    thermal_stability: float
    density: Optional[float] = None  # Added new property: density
    electrical_conductivity: Optional[float] = None  # Added new property: electrical conductivity

# Mock prediction model
def mock_polymer_prediction(structure: str, additives: List[str], temperature: float) -> PolymerProperties:
    """
    Mock function to simulate polymer property predictions based on input parameters.

    Args:
        structure (str): The chemical structure or identifier of the polymer.
        additives (List[str]): List of additives used in the polymer.
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
    density = random.uniform(0.9, 1.5)  # Simulated density prediction
    electrical_conductivity = random.uniform(0.01, 1.0)  # Simulated electrical conductivity prediction

    return PolymerProperties(
        glass_transition_temp=round(glass_transition_temp, 2),
        mechanical_strength=round(mechanical_strength, 2),
        thermal_stability=round(thermal_stability, 2),
        density=round(density, 2),
        electrical_conductivity=round(electrical_conductivity, 2)
    )

# Prediction service
def predict_properties(polymer_input: PolymerInput) -> dict:
    """
    Service function to predict polymer properties based on input data.
    
    Args:
        polymer_input (PolymerInput): Input data for prediction containing structure, additives, and temperature.
    
    Returns:
        dict: Dictionary of predicted polymer properties.
    """
    # Use the mock model function to predict properties
    predictions: PolymerProperties = mock_polymer_prediction(
        structure=polymer_input.structure,
        additives=polymer_input.additives,
        temperature=polymer_input.temperature
    )
    
    # Convert the PolymerProperties object to a dictionary for JSON serialization
    return predictions.dict()

# Example usage
if __name__ == "__main__":
    input_data = PolymerInput(structure="C6H12O6", additives=["Plasticizer", "Stabilizer"], temperature=150.0)
    result = predict_properties(input_data)
    print(result)
