"""
kafka consumer for "interesting" topic

here consumes messages and saves them to mongodb with timestamp
"""

from kafka import KafkaConsumer
import json
from datetime import datetime, timezone
from .db import collection
from app.utils import get_logger

logger = get_logger("consumer_interesting")

consumer = KafkaConsumer(
    "interesting",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="subscriber_interesting"
)


def consume_messages():
    """
    now its listen to kafka topic and insert messages into mongodb
    """
    for msg in consumer:
        try:
            data = msg.value
            data["timestamp"] = datetime.now(timezone.utc).isoformat()
            collection.insert_one(data)
            logger.info("Saved message with timestamp.")
        except Exception as e:
            logger.error(f"Failed to consume message: {e}")