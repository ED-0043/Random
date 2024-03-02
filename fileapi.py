from fastapi import FastAPI
from typing import List
from modelnlp import SentimentAnalyser

app = FastAPI()
model = SentimentAnalyser()

@app.get("/items/{items_id}")
def home(items_id):
    return {"items_id": items_id}

# @app.get()
# def get_item():
#     return {model.dataframer()}

# @app.post()
# def post_item():
#     return {model.preprocess_text()}

# @app.post()
# def post_item():
#     return {model.return_predictions()}

model.clean_data()
model.readablility_score()