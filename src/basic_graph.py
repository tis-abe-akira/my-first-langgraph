from langgraph.graph import Graph
from utils import save_mermaid_to_html

def node_a(input):
    input += " a"
    return input

def node_b(input):
    input += " b"
    return input

graph = Graph()

graph.add_node("node_a", node_a)
graph.add_node("node_b", node_b)
graph.set_entry_point("node_a")
graph.set_finish_point("node_b")
graph.add_edge("node_a", "node_b")
runner = graph.compile()

# Mermaid記法のGraph図を生成
mermaid_code = runner.get_graph().draw_mermaid()

# Mermaid記法のGraph図をHTMLファイルに出力
save_mermaid_to_html(mermaid_code, "out/basic_graph.html")
