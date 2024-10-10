from fastapi import FastAPI
from app.routers import prediction, maintenance

app = FastAPI(
    title="PolymerAI",
    description="AI backend for polymer property prediction",
    version="1.0.0",
)

# Include routes
app.include_router(prediction.router)
app.include_router(maintenance.router)

@app.get("/")
async def root():
    return {"message": "Welcome to PolymerAI!"}
