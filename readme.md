# Sample Application


## Setup and run application using python
1. Ensure you have Python 3.8 or higher installed.
2. Navigate to the `rag-demo` directory:
   ```bash
   cd rag-demo
   ```
## Create a virtual environment to isolate your project dependencies. you can use any of the below method to create vrtual environement.

### Create virutal environment using python

   1. Create virtual environment 

   **For macOS/Linux:**
   ```
   bash
   python3 -m venv venv
   ```

   **For Windows::**
   ```
   python -m venv venv
   ```

   2. Activate virtual environment

   **For macOS/Linux:**
   ```
   bash
   source venv/bin/activate
   ```

   **For Windows::**
   ```
   venv\Scripts\activate
   ```
## Create virtual environment using conda, ben

   1. Create conda virtual environment 
   ```
   conda create -n venv1 python=3.12 -y

   ```
   2. Activate conda virtual environment
   ```
   conda activate vevn1

   ```
   3. Deactivate conda virtual environment
   ```
   conda deactivate

   ```


## Install the required dependencies:

   ```
   pip install -r requirement.txt
   ```

## Run the application using uvicorn:

    ```
    uvicorn main:app --reload
    ```

## We created shell script run all above commands in on go, for anaconda


1. Make the `run_with_conda.sh` script executable (only required once):
   ```
   chmod +x run_with_conda.sh
   ```

2. Run the application using the script:
   ```
   ./run_with_conda.sh
   ```

## For core python

1. Make the `run_with_python.sh` script executable (only required once):
   ```
   chmod +x run_with_python.sh
   ```

2. Run the application using the script:
   ```
   ./run_with_python.sh
   ```

## you can use conda environment file to create environemnt and application

```
conda env create -f environment.yml

conda activate local

conda deactivate

```

 
## Once you are inside conda environment, run jupyter note book using belo command
```
jupyter lab
```

