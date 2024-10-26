from app.models.polymer_model import mock_polymer_prediction
from app.schemas.polymer import PolymerInput
from app.models.polymer_model import PolymerProperties

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
