from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import balance_sheet

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:3002", "http://localhost:3003"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
"""
Sets up CORS middleware to allow requests from specified origins.

Args:
- None (Middleware is configured directly within the app).

Returns:
- None (Middleware configuration does not return any value).
"""

app.include_router(balance_sheet.router)
"""
Includes the balance_sheet router to handle balance sheet-related endpoints.

Args:
- None (Router is included directly within the app).

Returns:
- None (Router inclusion does not return any value).
"""

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.

    Args:
    - None.

    Returns:
    - dict: A dictionary containing a welcome message for the root endpoint.
    """
    return {"message": "Welcome to your FastAPI application!"}

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    """
    Custom handler for 404 errors, returns a JSON response with an error message.

    Args:
    - request (Request): The incoming request object.
    - exc: The exception instance for the 404 error.

    Returns:
    - JSONResponse: A JSON response with a 404 status code and an error message.
    """
    return JSONResponse(
        status_code=404,
        content={"message": "Unknown endpoint"},
    )
