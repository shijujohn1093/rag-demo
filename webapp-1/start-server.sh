#!/bin/bash
PORT=${1:-8000}  # default to 8000 if no argument

# Run the application with uvicorn
uvicorn main:app --reload --port $PORT