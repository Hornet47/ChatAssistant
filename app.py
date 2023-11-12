from time import sleep
from openai import OpenAI
from assistants import Assistant
import functions

client = OpenAI().beta

assistant = Assistant(
    tools=[
        {"type": "code_interpreter"},
        {
            "type": "function",
            "function": functions.get_current_weather,
        },
    ]
)

print(assistant.id)

def submit_message(assistant_id, thread, user_message):
    client.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )


def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        sleep(0.5)
    return run
