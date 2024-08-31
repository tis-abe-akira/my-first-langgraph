import os
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from langgraph.graph import END

from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

@tool
def fake_database_api(query: str) -> str:
    """パーソナル情報を格納したデータベースを検索するAPI"""
    return "にんちゃは毎日８時間寝ます"

class State(TypedDict):
    messages: Annotated[list, add_messages]


llm = ChatOpenAI(temperature=0.5, max_tokens=100, model="gpt-4o")
llm_with_tools = llm.bind_tools([fake_database_api])

def llm_agent(state):
    state["messages"].append(llm_with_tools.invoke(state["messages"]))
    return state

def tool(state):
    tool_by_name = {"fake_database_api": fake_database_api}
    last_message = state["messages"][-1]
    tool_function = tool_by_name[last_message.tool_calls[0]["name"]]
    tool_output = tool_function.invoke(last_message.tool_calls[0]["args"])
    state["messages"].append(ToolMessage(content=tool_output, tool_call_id=last_message.tool_calls[0]["id"]))
    return state

def router(state):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tool"
    else:
        return "__end__"
    
graph = StateGraph(State)

graph.add_node("llm_agent", llm_agent)
graph.add_node("tool", tool)

graph.set_entry_point("llm_agent")
graph.add_conditional_edges("llm_agent",
                            router,
                            {"tool": "tool", "__end__": END})
graph.add_edge("tool", "llm_agent")
runner = graph.compile()

def get_response(query: str):
    response = runner.invoke({"messages": [query]})
    print(response)
    return response["messages"][-1].content

result = get_response("Hello, World!")
print(result)
print("")
result = get_response("にんちゃは何時間寝ますか？")
print(result)

