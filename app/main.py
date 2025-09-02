from fastapi import FastAPI
from .dbConn import conn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Dockerized FastAPI with Uvicorn!"}