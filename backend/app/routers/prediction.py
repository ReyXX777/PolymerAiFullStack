from fastapi import APIRouter, HTTPException
from app.schemas.polymer import PolymerInput, PolymerProperties  # Ensure PolymerProperties is defined in your schema
from app.services.prediction_service import predict_properties

router = APIRouter()

@router.post("/predict/", response_model=PolymerProperties)
async def predict_polymers(polymer_input: PolymerInput):
    """
    Endpoint to predict polymer properties based on the provided input data.
    
    Args:
        polymer_input (PolymerInput): Input data including structure, additives, and temperature.
    
    Returns:
        JSON response with predicted polymer properties.
    """
    try:
        # Call the prediction service to get property predictions
        predictions = predict_properties(polymer_input)
        return predictions
    except ValueError as ve:
        # Handle validation-specific errors
        raise HTTPException(status_code=422, detail=f"Validation error: {str(ve)}")
    except Exception as e:
        # Handle other unforeseen errors
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")
