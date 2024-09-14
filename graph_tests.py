from graph import Graph
from graph_utils import find_shortest_path

# Run tests
def test_graph():
    # Create a graph
    graph = Graph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Add edges
    graph.add_edge("A", "C")
    graph.add_edge("C", "B")
    graph.add_edge("B", "D")

    # Find a path from A to D
    assert find_shortest_path(graph, "A", "D") == ['A', 'C', 'B', 'D']

    # Edge case: Find a path from A to A
    assert find_shortest_path(graph, "A", "A") == ['A']

    # Edge case: Find a path from A to X
    assert find_shortest_path(graph, "A", "X") == None


    # Add more vertices
    graph.add_vertex("E")

    # Add more edges
    graph.add_edge("D", "E")
    graph.add_edge("A", "E")

    # Find a path from A to E
    assert find_shortest_path(graph, "A", "E") == ['A', 'E']

    print("All graph tests pass")


