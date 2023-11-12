from openai import OpenAI
from threads import Thread

client = OpenAI().beta


class Message:
    content: str
    thread: Thread

    def __init__(
        self,
        thread: Thread, 
        content: str
    ):
        self.content = content
        self.thread = thread
        
class UserMessage(Message):
    id: str
    
    
    def __init__(
        self,
        thread: Thread, 
        content: str
    ):
        super().__init__(thread, content)
        self._message = client.threads.messages.create(
            thread_id=thread.id, role="user", content=content
        )
        self.id = self._message.id
        
        
        
        
