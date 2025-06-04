from dotenv import load_dotenv
import textwrap
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

load_dotenv()

def create_code_reviewer() -> ChatAgent:
    """Creates a single agent specialized in code review."""
    system_message = textwrap.dedent(
        """
        You are an experienced senior software engineer who specializes in code review.
        Your role is to:
        1. Analyze code for bugs, security issues, and performance problems
        2. Check coding standards and best practices
        3. Suggest improvements for readability and maintainability
        4. Provide constructive feedback with specific examples

        Always be thorough but constructive in your feedback.
        Rate the code quality on a scale of 1-10 and explain your reasoning.
        """
    )

    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O,
    )

    agent = ChatAgent(
        system_message=BaseMessage.make_assistant_message(
            role_name="Senior Code Reviewer",
            content=system_message
        ),
        model=model,
    )

    return agent
