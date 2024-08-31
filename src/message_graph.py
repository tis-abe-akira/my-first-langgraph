from langgraph.graph import MessageGraph
from langchain_core.messages import HumanMessage

def node_a(input):
    input[0].content += " a"
    return input

def node_b(input):
    input[0].content += " b"
    return input

graph = MessageGraph()
graph.add_node("node_a", node_a)
graph.add_node("node_b", node_b)
graph.set_entry_point("node_a")
graph.set_finish_point("node_b")
graph.add_edge("node_a", "node_b")

runner = graph.compile()
result = runner.invoke("Hello, World!")
print(result)

