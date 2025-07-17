#!/bin/bash
PORT=${1:-8000}  # default to 8000 if no argument

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirement.txt

# Run the application with uvicorn
uvicorn main:app --reload --port $PORT