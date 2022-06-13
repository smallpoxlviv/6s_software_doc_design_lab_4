import json
import os

from .send_text import SendText
from kafka import KafkaProducer

host = os.getenv('k_host', default='localhost')
port = os.getenv('k_port', default='1234')
topic = os.getenv('k_topic', default='test')


class SendTextKafka(SendText):
    @classmethod
    def send_text(cls, text_list: list[dict]):
        producer = KafkaProducer(bootstrap_servers=f'{host}:{port}')
        for text in text_list:
            producer.send(topic, json.dumps(text))
