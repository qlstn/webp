from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

name = "subin"
 
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def read_root():
    return {"Hello": "World"}

@app.update("/")
def update_root():
    return {"Hello": "World"}

@app.delete("/")
def delete_root():
    return {"Hello": "World"}

