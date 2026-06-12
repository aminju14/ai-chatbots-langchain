import os
import getpass
from dotenv import load_dotenv

# pyrefly: ignore [missing-import]
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Load API key dari file .env (jika ada)
load_dotenv()

# Jika tidak ada di .env, minta input manual
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API Key: ")

client = ChatOpenAI(model="gpt-4o-mini")

print("LLM is ready!")
chat_history = [SystemMessage("You are a comedian")]

while True:
    prompt = input("User: ")
    print()
    chat_history.append(HumanMessage(prompt))
    response = client.invoke(chat_history)
    print("AI:", response.content)
    print()