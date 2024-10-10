from app.models.polymer_model import mock_polymer_prediction

def predict_properties(polymer_input):
    return mock_polymer_prediction(
        polymer_input.structure, 
        polymer_input.additives, 
        polymer_input.temperature
    )
