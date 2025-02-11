import random
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PolymerProperties(BaseModel):
    """Class representing polymer properties."""
    glass_transition_temp: float
    mechanical_strength: float
    thermal_stability: float
    density: Optional[float] = None
    electrical_conductivity: Optional[float] = None
    molecular_weight: Optional[float] = None  # Added new property: molecular weight
    crystallinity: Optional[float] = None  # Added new property: crystallinity
    solubility: Optional[float] = None  # Added new property: solubility
    viscosity: Optional[float] = None  # Added new property: viscosity
    biodegradability: Optional[float] = None  # Added new property: biodegradability

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
    density = random.uniform(0.9, 1.5)
    electrical_conductivity = random.uniform(0.01, 1.0)
    molecular_weight = random.uniform(1000, 100000)  # Simulated molecular weight prediction
    crystallinity = random.uniform(0, 100)  # Simulated crystallinity prediction
    solubility = random.uniform(0, 1)  # Simulated solubility prediction
    viscosity = random.uniform(100, 10000)  # Simulated viscosity prediction
    biodegradability = random.uniform(0, 100)  # Simulated biodegradability prediction

    return PolymerProperties(
        glass_transition_temp=round(glass_transition_temp, 2),
        mechanical_strength=round(mechanical_strength, 2),
        thermal_stability=round(thermal_stability, 2),
        density=round(density, 2),
        electrical_conductivity=round(electrical_conductivity, 2),
        molecular_weight=round(molecular_weight, 2),
        crystallinity=round(crystallinity, 2),
        solubility=round(solubility, 2),
        viscosity=round(viscosity, 2),
        biodegradability=round(biodegradability, 2)
    )

def save_prediction_to_file(prediction: PolymerProperties, filename: str = "polymer_prediction.txt"):
    """
    Save the predicted polymer properties to a file.

    Args:
        prediction (PolymerProperties): The predicted polymer properties.
        filename (str): The name of the file to save the prediction.
    """
    with open(filename, "a") as file:
        file.write(f"Prediction Time: {datetime.now()}\n")
        file.write(f"Glass Transition Temperature: {prediction.glass_transition_temp} K\n")
        file.write(f"Mechanical Strength: {prediction.mechanical_strength} MPa\n")
        file.write(f"Thermal Stability: {prediction.thermal_stability} K\n")
        file.write(f"Density: {prediction.density} g/cm³\n")
        file.write(f"Electrical Conductivity: {prediction.electrical_conductivity} S/m\n")
        file.write(f"Molecular Weight: {prediction.molecular_weight} g/mol\n")
        file.write(f"Crystallinity: {prediction.crystallinity} %\n")
        file.write(f"Solubility: {prediction.solubility} g/L\n")
        file.write(f"Viscosity: {prediction.viscosity} cP\n")
        file.write(f"Biodegradability: {prediction.biodegradability} %\n")
        file.write("\n")

# Example usage
if __name__ == "__main__":
    structure = "C6H12O6"
    additives = ["Plasticizer", "Stabilizer"]
    temperature = 150.0

    predicted_properties = mock_polymer_prediction(structure, additives, temperature)
    print(predicted_properties)
    save_prediction_to_file(predicted_properties)
