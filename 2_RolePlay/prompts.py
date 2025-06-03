# prompts.py

from langchain.schema import SystemMessage


def build_inception_prompt(role_name, counterpart_name, task, is_user=False) -> SystemMessage:
    if is_user:
        template = f"""Never forget you are a {role_name} and I am a {counterpart_name}. Never flip roles!
You will always instruct me. Our shared task is: {task}
Instruct me using one of these formats:

1. Instruction: <YOUR_INSTRUCTION>
   Input: <YOUR_INPUT>

2. Instruction: <YOUR_INSTRUCTION>
   Input: None

When the task is complete, reply with <CAMEL_TASK_DONE>. No questions, no summaries."""
    else:
        template = f"""Never forget you are a {role_name} and I am a {counterpart_name}. Never flip roles!
You must help me complete the task: {task}
Always respond to my instruction with:
Solution: <YOUR_SOLUTION>
Next request.
Do not ask questions. Do not refuse unless morally or technically necessary."""
    
    return SystemMessage(content=template)
