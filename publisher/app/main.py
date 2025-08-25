"""
fastapi publisher service

and publishes messages from 20newsgroups dataset to Kafka.
"""

from fastapi import FastAPI
from app.dataset import load_messages
from app.producer import publish_messages

app = FastAPI()

@app.get("/")
def root():
    return {"message": "publisher is running"}


@app.get("/publish")
def publish():
    """
    are its fetch 20 messages and publish them to kafka
    """
    messages = load_messages()
    publish_messages(messages)
    return {"status": "published", "count": len(messages)}