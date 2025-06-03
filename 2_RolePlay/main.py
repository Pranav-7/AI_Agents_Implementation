# main.py

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from camel_agent import CAMELAgent
from prompts import build_inception_prompt

# Load .env for API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not found. Set it in .env file.")

# Define task and roles
task = "Create a basic 2D platformer character controller in Unity with jump and collision handling"
user_role = "Game Designer"
assistant_role = "Unity Developer"

# Initialize model
model = ChatOpenAI(model_name="gpt-4", temperature=0.2)

# Build agents
user_sys_msg = build_inception_prompt(user_role, assistant_role, task, is_user=True)
assistant_sys_msg = build_inception_prompt(assistant_role, user_role, task, is_user=False)

user_agent = CAMELAgent(system_message=user_sys_msg, model=model)
assistant_agent = CAMELAgent(system_message=assistant_sys_msg, model=model)

# Start conversation
turn_limit = 20
turn = 0
msg = HumanMessage(content="Start task")

while turn < turn_limit:
    assistant_msg = assistant_agent.step(msg)
    print(f"\n{assistant_role}:\n{assistant_msg.content}\n")

    user_msg = user_agent.step(assistant_msg)
    print(f"{user_role}:\n{user_msg.content}\n")

    if "<CAMEL_TASK_DONE>" in user_msg.content:
        print("✅ Task completed.")
        break

    msg = user_msg
    turn += 1
