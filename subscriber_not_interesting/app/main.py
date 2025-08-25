"""
initializ fastapi subscriber service for "not_interesting" topic
"""
from fastapi import FastAPI
from .db import collection

app = FastAPI()


@app.get("/")
def root():
    return {"message": "subscriber (not_interesting) is running"}



@app.get("/messages")
def get_messages():
    """
    and return all stored messages from mongodb
    """