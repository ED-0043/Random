from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
from .model import Model

class Item(BaseModel):
    name: str
    date: str
    age: int
    phone_num: Optional[int]

app = FastAPI()
model = Model()

@app.post(path=Path(description="unknown destination"))
def post_item():
    return {
        model.forward()
        }

@app.post(path=Path(description="unkown destination"))
def post_item():
    return{model.forward}
