from camel.messages import BaseMessage
from reviewer_agent import create_code_reviewer

sample_code = """
def calculate_total(items):
    total = 0
    for item in items:
        if item['price'] > 0:
            total = total + item['price']
    return total

def process_order(order_data):
    items = order_data['items']
    total = calculate_total(items)
    if total > 100:
        discount = total * 0.1
        total = total - discount
    print(f"Order total: ${total}")
    return total
"""

def main():
    reviewer = create_code_reviewer()

    review_request = f"""
    Please review the following Python code:

    {sample_code}

    Focus on:
    - Code quality and best practices
    - Potential bugs or issues
    - Performance considerations
    - Suggestions for improvement
    """

    response = reviewer.step(BaseMessage.make_user_message(
        role_name="Developer",
        content=review_request
    ))

    print("=== SINGLE AGENT CODE REVIEW ===")
    print(response.msg.content)

if __name__ == "__main__":
    main()
