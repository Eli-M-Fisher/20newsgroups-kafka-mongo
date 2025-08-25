"""
here is the kafka producer that sends messages to topics
"""

from kafka import KafkaProducer
import json
from app.utils import get_logger


logger = get_logger("producer")

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def publish_messages(messages):
    """
    here I publish list of (topic, text) messages to kafka
    """
    for topic, text in messages:
        try:
            producer.send(topic, {"text": text})
            logger.info(f"Sent message to topic: {topic}")
        except Exception as e:
            logger.error(f"Failed to send message: {e}")

    producer.flush()