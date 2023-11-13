from openai import OpenAI
from assistants import Assistant
from threads import Thread
import functions

client = OpenAI().beta

assistant = Assistant(
    tools=[
        {"type": "code_interpreter"},
        {
            "type": "function",
            "function": functions.d_get_current_weather,
        },
    ]
)

initial_message = input("Send a message:")
thread = Thread(initial_message, assistant)

while True:
    thread.wait_on_run()
    
    if thread.run.status == "requires_action":
        thread.submit_tool_outputs()
        thread.wait_for_complete()
        
    print("Assistant: " + thread.get_response())
    message = input("Send a message: ")
    thread.add_and_run(message, assistant)