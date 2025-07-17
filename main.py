from fastapi import FastAPI
from dotenv import load_dotenv
import os
import time
import asyncio
from app.controllers import example_controller


# Load the appropriate .env file based on the environment
environment = os.getenv("ENVIRONMENT", "local")  # Default to 'local'
env_file = f"env/.env.{environment}"
load_dotenv(env_file)

app = FastAPI()

# Include routers
app.include_router(example_controller.router, prefix="/api/v1")

@app.get("/env")
def read_root():
    return {
        "message": "Hello, FastAPI!",
        "environment": environment,
        "loaded_env_file": env_file
    }




"""
Runs in main thread 
No awaiteable operations, cannot be paused
Sequentioal order
Request 1
    Hello
    Bye
Request 2
    Hello
    Bye

"""
@app.get("/1")
async def endpoint1(): # Processed sequentially 
    print("Hello")
    time.sleep(5) # Blocking I/O operation, cannot be awaited
    # Function execution cannot be paused
    print("Bye") 


"""
Runs in main thread 
Has awaitable operaion, can be paused

Request 1
    Hello
Request 2
    Hello
Request 1
    Bye
Request 2
    Bye
"""
@app.get("/2")
async def endpoint2():    # Processed Concurrently
    print("Hello")
    await asyncio.sleep(5)    # Non-blocking I/O operation, can be awaited
    # Function execution paused
    print("Bye")


"""
Runs in separate thread, this is the reason all the processing done parallelly
"""
@app.get("/3")
def endpoint3():
    print("Hello")
    time.sleep(5)
    print("Bye")
    

"""
BEST PRACTICES
1. Use async def for endpoint with non blocking I/O operations.
2. Dont use async def for the endpoint blocking I/O operations.
3. Use normal function for endpoints with blocking I/O operations
"""