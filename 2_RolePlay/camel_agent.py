# camel_agent.py

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from typing import List


class CAMELAgent:
    def __init__(self, system_message: SystemMessage, model: ChatOpenAI):
        self.system_message = system_message
        self.model = model
        self.reset()

    def reset(self):
        self.stored_messages: List = [self.system_message]

    def update_messages(self, msg):
        self.stored_messages.append(msg)
        return self.stored_messages

    def step(self, input_msg: HumanMessage):
        self.update_messages(input_msg)
        output_msg = self.model(self.stored_messages)
        self.update_messages(output_msg)
        return output_msg
