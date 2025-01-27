# PolymerAiFullStack/backend/app/__init__.py

from fastapi import FastAPI
from .routers import polymer_router
from .middleware import log_requests_middleware
from .config import settings

# Initialize the FastAPI application
app = FastAPI(
    title="Polymer AI Backend",
    description="Backend service for polymer property predictions",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Add middleware for logging requests
app.middleware("http")(log_requests_middleware)

# Include the polymer router
app.include_router(polymer_router.router, prefix="/api/v1/polymers", tags=["polymers"])

# Health check endpoint
@app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy", "version": app.version}

# Root endpoint
@app.get("/", tags=["root"])
def root():
    return {"message": "Welcome to the Polymer AI Backend!"}

# Application startup event
@app.on_event("startup")
async def startup_event():
    print("Starting Polymer AI Backend...")
    # Add any startup logic here, such as initializing databases or loading models

# Application shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down Polymer AI Backend...")
    # Add any cleanup logic here
