# setting the environment variables, the keys
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from config import set_environment
# for the keys - as explained early in chapter 2
set_environment()

from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai.chat_models import ChatOpenAI

openai_llm = OpenAI()

chat = ChatOpenAI(model_name='gpt-4o')

messages = [
    SystemMessage(content="you're a helpful programming assistant"),
    HumanMessage(content="Wite a Python function to calculate factorial")
]
response = chat.invoke(messages)
print(response)