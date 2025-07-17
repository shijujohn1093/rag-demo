from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.controllers import example_controller


# Load the appropriate .env file based on the environment
environment = os.getenv("ENVIRONMENT", "local")  # Default to 'local'
env_file = f"env/.env.{environment}"
load_dotenv(env_file)

app = FastAPI()

# Include routers
app.include_router(example_controller.router, prefix="/api/v1")

@app.get("/env")
def read_root():
    return {
        "message": "Hello, FastAPI!",
        "environment": environment,
        "loaded_env_file": env_file
    }