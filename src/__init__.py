from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Here we determine which events to run at startup and shutdown.
    ## The code above yield is going to run at the start of our application, 
    ## while the code below yield is going to run when our application shutsdown.
    print("Starting up the application...")
    yield 
    print("Shutting down the application...")

app = FastAPI(
    title="SQL Project API",
    description="API for managing SQL projects",
    version="1.0.0",
    lifespan=lifespan
) 