"""
FastAPI application main entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import users, courses, assignments, bookings

# Create FastAPI app
app = FastAPI(
    title="Smart Campus Connect API",
    description="REST API for Smart Campus Connect - Student Lifecycle Management Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(assignments.router)
app.include_router(bookings.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Smart Campus Connect API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}