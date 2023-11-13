from typing import List
from openai import OpenAI
from openai.types.beta.threads.run import Run
from openai.types.beta.threads.thread_message import ThreadMessage
from assistants import Assistant
import time
import toolcalls

client = OpenAI().beta


class Thread:
    id: str
    run: Run
    messages: List[ThreadMessage]

    def __init__(self, init_message: str, assistant: Assistant):
        self._thread = client.threads.create()
        self.id = self._thread.id
        self.messages = []
        self.add_and_run(init_message, assistant)

    def add_and_run(self, content: str, assistant: Assistant) -> Run:
        message = client.threads.messages.create(self.id, content=content, role="user")
        self.messages.append(message)
        self.run = client.threads.runs.create(thread_id=self.id, assistant_id=assistant.id)
        return self.run

    def wait_on_run(self) -> Run:
        while self.run.status == "queued" or self.run.status == "in_progress":
            time.sleep(0.2)
            self.run = client.threads.runs.retrieve(
                run_id=self.run.id,
                thread_id=self.id
            )
        return self.run
    
    def wait_for_complete(self) -> Run:
        while self.run.status != "completed":
            time.sleep(0.2)
            self.run = client.threads.runs.retrieve(
                run_id=self.run.id,
                thread_id=self.id
            )
        return self.run
            
    def get_response(self) -> str:
            message = client.threads.messages.list(self.id).data[0]
            self.messages.append(message)
            return message.content[0].text.value
        
    def submit_tool_outputs(self):
        _toolcalls = self.run.required_action.submit_tool_outputs.tool_calls
        outputs = toolcalls.execute_all(_toolcalls)
        client.threads.runs.submit_tool_outputs(
            run_id=self.run.id, 
            thread_id=self.id, 
            tool_outputs=outputs
            )
        
