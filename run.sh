#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the application with uvicorn
uvicorn main:app --reload