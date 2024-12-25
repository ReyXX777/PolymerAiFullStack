from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers import prediction, maintenance
from app.config import get_config
from app.database import initialize_db  # Assuming you have a database module for setup

# Initialize app with settings
app = FastAPI(
    title="PolymerAI",
    description="AI backend for polymer property prediction",
    version="1.0.0",
)

# Load configuration
config = get_config()

# CORS Middleware - Adjust allowed origins as per your requirements
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database if necessary
@app.on_event("startup")
async def startup_event():
    """
    Event triggered at app startup. Use it for tasks like database initialization.
    """
    initialize_db()

# Include prediction and maintenance routers
app.include_router(prediction.router, prefix="/api/prediction", tags=["Prediction"])
app.include_router(maintenance.router, prefix="/api/maintenance", tags=["Maintenance"])

# Root route
@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint with a welcome message.
    """
    return {"message": "Welcome to PolymerAI!"}

# Health check route
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify service availability.
    """
    return {"status": "healthy"}

# Error handling
@app.exception_handler(404)
async def not_found_error(request: Request, exc):
    """
    Custom handler for 404 errors.
    """
    return JSONResponse(status_code=404, content={"error": "Resource not found"})

@app.exception_handler(500)
async def internal_error(request: Request, exc):
    """
    Custom handler for 500 internal server errors.
    """
    return JSONResponse(status_code=500, content={"error": "An internal error occurred"})
