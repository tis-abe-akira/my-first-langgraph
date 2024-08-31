import getpass
import os
from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

llm = ChatOpenAI(temperature=0.5, max_tokens=100, model="gpt-4o")

class State(TypedDict):
    messages: Annotated[list, add_messages]
    api_call_count: int

def chatbot(state: State):
    if not state["api_call_count"]:
        state["api_call_count"] = 0
    state["api_call_count"] += 1
    return {"messages": [llm.invoke(state["messages"])], "api_call_count": state["api_call_count"]}

graph = StateGraph(State)

graph.add_node("chatbot", chatbot)
graph.set_entry_point("chatbot")
graph.set_finish_point("chatbot")
runner = graph.compile()

response = runner.invoke({"messages": ["Hello, World!"], "api_call_count": 1})
print(response)

print("***")
print(response["messages"][-1].content)
print("***")
print(response["api_call_count"])
