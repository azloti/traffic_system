from graph import Graph

# Find shortest path from start to end in a graph
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.vertices:
        return None
    shortest = None
    for vertex in graph.vertices[start]:
        if vertex not in path:
            newpath = find_shortest_path(graph, vertex, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest