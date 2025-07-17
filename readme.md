# Project Title

Create a virtual environment to isolate your project dependencies.

## Creating a Virtual Environment

1. Ensure you have Python 3.8 or higher installed.
2. Navigate to the `rag-demo` directory:
   ```bash
   cd rag-demo
3. Run the following commands to create and activate a virtual environment:

   **For macOS/Linux:**
   ```
   bash
   python3 -m venv venv
   source venv/bin/activate
    ```
   **For Windows::**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Run the application using uvicorn:

    ```
    uvicorn main:app --reload
    ```



## Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:

```bash
deactivate


