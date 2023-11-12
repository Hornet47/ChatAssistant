from typing import List
from openai import OpenAI
from messages import Message, UserMessage

client = OpenAI().beta


class Thread:
    id: str
    messages: List[Message]

    def __init__(self):
        self._thread = client.threads.create()
        self.id = self._thread.id

    def add_user_message(self, message: str):
        self.messages.append(UserMessage(self, message))

    def get_last_message(self) -> Message:
        message = client.threads.messages.list(self.id).data[0].content[0].text.value
        return message
