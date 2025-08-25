"""
fastapi subscriber service for "interesting" topic
"""

from fastapi import FastAPI
from .db import collection

app = FastAPI()

@app.get("/")
def root():
    return {"message": "subscriber (interesting) is running"}


@app.get("/messages")
def get_messages():
    """
    and here return all stored messages from mongodb
    """
    msgs = list(collection.find({}, {"_id": 0}))
    return {"messages": msgs}