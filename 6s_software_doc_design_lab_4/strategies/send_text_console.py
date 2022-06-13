import json

from .send_text import SendText


class SendTextConsole(SendText):
    @classmethod
    def send_text(cls, text_list: list):
        for text in text_list:
            print(json.dumps(text))
