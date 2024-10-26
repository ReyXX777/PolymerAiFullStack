from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
    # Initialize database connection and tables if needed
    initialize_db()

# Include prediction and maintenance routers
app.include_router(prediction.router)
app.include_router(maintenance.router)

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to PolymerAI!"}

# Health check route
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Error handling (optional)
@app.exception_handler(404)
async def not_found_error(request, exc):
    return {"error": "Not found"}

@app.exception_handler(500)
async def internal_error(request, exc):
    return {"error": "An internal error occurred"}

