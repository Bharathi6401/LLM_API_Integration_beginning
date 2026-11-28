# Controlling response format
import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
    )
messages = [
    {
        "role": "system",
        "content": """
        You are a friendly Python tutor.

        Rules:
        - Answer only Python-related questions.
        - Explain concepts in beginner-friendly language.
        - Use simple examples.
        - If a question is unrelated to Python,
          politely explain that you only help with Python.

        Response format:
        - Keep answers concise.
        - Use bullet points wherever appropriate.
        - Use short code examples when necessary.
        - Avoid unnecessarily long explanations.
        """
    }
]

while True:
    question = input("Ask me anything: ").strip()

    if question.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": question
    })
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        response_format={"type":"json_object"}
    )

    answer = response.choices[0].message.content
    data=json.loads(answer)
    

    messages.append({
        "role": "assistant",
        "content": answer
    })

    print("\nAI:", answer)
# # Controlling response format
# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# import json
# load_dotenv()
# client = OpenAI(
#     api_key=os.getenv("GROQ_API_KEY"),
#     base_url="https://api.groq.com/openai/v1"
#     )
# messages = [
#     {
#         "role": "system",
#         "content": """
#         You are a friendly Python tutor.

#         Rules:
#         - Answer only Python-related questions.
#         - Explain concepts in beginner-friendly language.
#         - Use simple examples.
#         - If a question is unrelated to Python,
#           politely explain that you only help with Python.

#         Response format:
#         - Keep answers concise.
#         - Use bullet points wherever appropriate.
#         - Use short code examples when necessary.
#         - Avoid unnecessarily long explanations.
#         """
#     }
# ]

# while True:
#     question = input("Ask me anything: ").strip()

#     if question.lower() == "exit":
#         break

#     messages.append({
#         "role": "user",
#         "content": question
#     })
    
#     response = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=messages,
#         response_format={"type":"json_object"}
#     )

#     answer = response.choices[0].message.content
#     data=json.loads(answer)
    

#     messages.append({
#         "role": "assistant",
#         "content": answer
#     })

#     print("\nAI:", answer)
# System prompt
# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# load_dotenv()
# client = OpenAI(
#     api_key=os.getenv("GROQ_API_KEY"),
#     base_url="https://api.groq.com/openai/v1"
#     )
# messages = [
#     {
#         "role": "system",
#         "content": """
#         You are a friendly Python tutor.

#         Rules:
#         - Answer only Python-related questions.
#         - Explain concepts in beginner-friendly language.
#         - Use simple examples.
#         - If a question is unrelated to Python,
#           politely explain that you only help with Python.
#         """
#     }
# ]
# while True:
#     question = input("Ask me anything: ").strip()

#     if question.lower() == "exit":
#         break

#     messages.append({
#         "role": "user",
#         "content": question
#     })

#     response = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=messages
#     )

#     answer = response.choices[0].message.content

#     messages.append({
#         "role": "assistant",
#         "content": answer
#     })

#     print("\nAI:", answer)
# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# load_dotenv()
# client = OpenAI(
#     api_key=os.getenv("GROQ_API_KEY"),
#     base_url="https://api.groq.com/openai/v1"
#     )
# messages = [
#     {
#         "role": "system",
#         "content": "You are a friendly Python tutor."
#     }
# ]

# while True:
#     question = input("Ask me anything: ").strip()

#     if question.lower() == "exit":
#         break

#     messages.append({
#         "role": "user",
#         "content": question
#     })

#     response = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=messages
#     )

#     answer = response.choices[0].message.content

#     messages.append({
#         "role": "assistant",
#         "content": answer
#     })

#     print("\nAI:", answer)
# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()
# client = OpenAI(
#     api_key=os.getenv("GROQ_API_KEY"),
#     base_url="https://api.groq.com/openai/v1"
#     )
# while True:
#     # Get input from the user
#     question = input("Ask me anything: ")

#     if question.lower() == "exit":
#         break

#     # Send the question to the LLM
#     response = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a friendly Python tutor. Explain in simple words."
#             },
#             {
#                 "role": "user",
#                 "content": question
#             }
#         ]
#     )

#     # Display the LLM response
#     print("\nAI Response:")
#     print(response.choices[0].message.content)

# # import os
# # from dotenv import load_dotenv
# # from openai import OpenAI

# # load_dotenv()

# # client = OpenAI(
# #     api_key=os.getenv("GROQ_API_KEY"),
# #     base_url="https://api.groq.com/openai/v1"
# # )

# # response = client.chat.completions.create(
# #     model="openai/gpt-oss-20b",
# #     messages=[
# #         {
# #             "role": "system",
# #             "content": "You are a friendly Python tutor. Explain in simple words."
# #         },
# #         {
# #             "role": "user",
# #             "content": "What is a Python dictionary?"
# #         }
# #     ]
# # )
# # # Here:
# # # - System tells the model how to behave.It tells the AI how to behave and how to respond.

# # # For example:
# # # - system: "You are a beginner-friendly Python tutor. Keep answers short and simple."
# # # - user: "Explain Python decorators."
# # # So the system message controls the AI's response style, while the user message contains the actual question.
# # # - User provides the actual question.
# # # - Assistant generates the answer.
# # # system	Provides overall instructions and behavior
# # # user	Contains the user's question or input
# # # assistant	Represents the model's response

# # print(response.choices[0].message.content) 
# #                                             # Part	    Meaning
# #                                             # response	Complete response returned by the API
# #                                             # .choices	List of generated response choices
# #                                             # [0]	    Selects the first choice
# #                                             # .message	Contains the generated message
# #                                             # .content	Contains the actual text answer
# # # messages = [
# # #     {
# # #         "role": "system",
# # #         "content": "You are a Python tutor."
# # #     },
# # #     {
# # #         "role": "user",
# # #         "content": "What is a list?"
# # #     },
# # #     {
# # #         "role": "assistant",
# # #         "content": "A list is an ordered collection of items."
# # #     },
# # #     {
# # #         "role": "user",
# # #         "content": "Can you give an example?"
# # #     }
# # # ]
# # # Here, the previous assistant response is included as conversation history. This helps the model understand the ongoing conversation.

# # # Important: In our normal API request, we don't need to manually write the assistant response beforehand. The model generates it. 
# # # We include previous assistant messages when we want to send conversation history.