from abc import ABC, abstractmethod


class SendText(ABC):

    @classmethod
    @abstractmethod
    def send_text(cls, text: str):
        pass
