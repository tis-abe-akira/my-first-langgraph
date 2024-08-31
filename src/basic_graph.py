from langgraph.graph import Graph

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
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
</head>
<body>
    <div class="mermaid">
        {mermaid_code}
    </div>
</body>
</html>
"""

with open("graph.html", "w") as file:
    file.write(html_content)

print("Graph has been written to graph.html. Open this file in a web browser to view the graph.")
