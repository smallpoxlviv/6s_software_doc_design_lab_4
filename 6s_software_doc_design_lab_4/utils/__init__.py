import requests
from kafka import KafkaConsumer


def read_from_api(url: str):
    r = requests.get(url)
    return r.json()

