from openai import OpenAI
from threads import Thread
from assistants import Assistant

client = OpenAI().beta


class Run:
    id: str
    
    def __init__(
        self, 
        thread: Thread, 
        assistant: Assistant
    ):
        self._run = client.threads.runs.create(thread.id, assistant.id)
        self.id = self._run.id