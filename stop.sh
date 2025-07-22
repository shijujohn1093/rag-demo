#!/bin/bash

PORT=${1:-8000}  # default to 8000 if no argument

# Find PID of uvicorn running on the given port
PID=$(lsof -i :$PORT -sTCP:LISTEN -t | xargs ps -p | grep uvicorn | awk '{print $1}')

if [ -n "$PID" ]; then
  echo "Uvicorn process detected on port $PORT (PID $PID). Stopping it gracefully..."
  kill "$PID"
  sleep 2  # Wait for graceful shutdown
else
  echo "No uvicorn process running on port $PORT."
fi

# Deactivate Python venv if active
if [[ "$VIRTUAL_ENV" != "" ]]; then
  echo "Deactivating Python virtual environment..."
  deactivate
else
  echo "No Python venv is active."
fi

# Deactivate Conda env if active
if [[ "$CONDA_DEFAULT_ENV" != "" ]]; then
  echo "Deactivating Conda environment..."
  conda init
  conda deactivate
else
  echo "No Conda environment is active."
fi

echo "Server stopped. Note: If you activated Conda env in parent shell, deactivate manually if needed."
