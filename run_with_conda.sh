#!/bin/bash

PORT=${1:-8000}  # default to 8000 if no argument


conda create -n venv1 python=3.12 -y

conda init
# Activate the virtual environment
conda activate vevn1

# Install dependencies from requirements.txt
pip install -r requirement.txt

# Run the application with uvicorn
uvicorn main:app --reload --port $PORT