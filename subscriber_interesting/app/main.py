"""
fastapi subscriber service for "interesting" topic
"""


from fastapi import FastAPI
from .db import collection
from .consumer import consume_messages
import threading

app = FastAPI()

@app.on_event("startup")
def start_consumer():
    thread = threading.Thread(target=consume_messages, daemon=True)
    thread.start()

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