from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.post()
def post_item():
    return {}

@app.get()
def get_item():
    return {}

@app.post()
def post_item():
    return {}

@app.post()
def post_item():
    return {}