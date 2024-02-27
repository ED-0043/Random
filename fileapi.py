from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/items/{items_id}")
def home(items_id):
    return {"items_id": items_id}

# @app.get()
# def get_item():
#     return {}

# @app.post()
# def post_item():
#     return {}

# @app.post()
# def post_item():
#     return {}