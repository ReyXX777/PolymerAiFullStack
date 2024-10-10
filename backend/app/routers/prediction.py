from fastapi import APIRouter, HTTPException
from app.schemas.polymer import PolymerInput
from app.services.prediction_service import predict_properties

router = APIRouter()

@router.post("/predict/")
async def predict_polymers(polymer_input: PolymerInput):
    try:
        predictions = predict_properties(polymer_input)
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
