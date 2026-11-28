
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# 1. Python function
def calculate_discount(price, discount_percentage):
    discount = price * (discount_percentage / 100)
    final_price = price - discount
    return final_price


# 2. Tool definition
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_discount",
            "description": "Calculate the final price after applying a discount percentage",
            "parameters": {
                "type": "object",
                "properties": {
                    "price": {
                        "type": "number",
                        "description": "Original price of the product"
                    },
                    "discount_percentage": {
                        "type": "number",
                        "description": "Discount percentage to apply"
                    }
                },
                "required": ["price", "discount_percentage"]
            }
        }
    }
]


# 3. First API request
user_prompt = (
    "Calculate a 10% discount on 1000 rupees and a 20% "
    "discount on 2000 rupees. Use the function separately for each calculation."
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    tools=tools
)


# 4. Extract assistant message
message = response.choices[0].message

print("Number of tool calls:", len(message.tool_calls or []))


# 5. Execute every tool call
tool_results = []

for tool_call in message.tool_calls or []:

    print("Function:", tool_call.function.name)
    print("Arguments:", tool_call.function.arguments)

    arguments = json.loads(tool_call.function.arguments)

    if tool_call.function.name == "calculate_discount":

        result = calculate_discount(**arguments)

        print("Calculation result:", result)

        tool_results.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })


# 6. Build conversation history
messages = [
    {
        "role": "user",
        "content": user_prompt
    },
    message
]

messages.extend(tool_results)


# 7. Second API request
# 6. Prepare results for the final AI response

if tool_results:

    results_text = "\n".join(
        [
            f"Calculation {i + 1}: {item['content']}"
            for i, item in enumerate(tool_results)
        ]
    )

    # 7. Second API request
    final_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Use the calculation results provided by Python "
                    "to answer the user's question. "
                    "Do not perform additional calculations."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Original request: {user_prompt}\n\n"
                    f"Python calculation results:\n{results_text}\n\n"
                    "Explain the results clearly."
                )
            }
        ]
    )

    print("\nFinal AI Response:")
    print(final_response.choices[0].message.content)

else:
    print("The model did not request any tool calls.")
    print("AI Response:", message.content)