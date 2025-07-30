#!/bin/bash

conda create -n venv1 python=3.12 -y

conda init
# Activate the virtual environment
conda activate vevn1

# Install dependencies from requirements.txt
pip install -r requirement.txt