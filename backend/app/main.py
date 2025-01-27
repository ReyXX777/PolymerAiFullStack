from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers import prediction, maintenance
from app.config import get_config
from app.database import initialize_db  # Assuming you have a database module for setup
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

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

# Redirect HTTP to HTTPS in production
if config.ENV == "production":
    app.add_middleware(HTTPSRedirectMiddleware)

# Serve static files (e.g., docs, assets)
app.mount("/static", StaticFiles(directory="static"), name="static")

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

# Custom middleware for logging requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware to log incoming requests.
    """
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response
