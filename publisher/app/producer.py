"""
here is the kafka producer that sends messages to topics
"""

from kafka import KafkaProducer
import json
from app.utils import get_logger

def publish_messages(messages):
    """
    here I publish list of (topic, text) messages to kafka
    """