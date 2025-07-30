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

## Install the required dependencies:

   ```
   pip install -r requirement.txt
   ```


## Create virtual environment using conda, 

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

## You can use conda environment file to create environemnt and application, It will download all the dependencies when environment is created and give you ready to use environment

```
conda env create -f environment.yml

conda activate local

conda deactivate

```

## Once you are inside conda environment, run jupyter note book using belo command
```
jupyter lab
```

## Or you can run web application using below command

 ```
 uvicorn main:app --reload
 ```





 

