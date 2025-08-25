"""
kafka consumer for "interesting" topic

here consumes messages and saves them to mongodb with timestamp
"""

from kafka import KafkaConsumer
import json
from datetime import datetime
from .db import collection
from app.utils import get_logger

logger = get_logger("consumer_interesting")

def consume_messages():
    """
    now its listen to kafka topic and insert messages into mongodb
    """