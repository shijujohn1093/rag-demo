#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirement.txt

# Run the application with uvicorn
uvicorn main:app --reload