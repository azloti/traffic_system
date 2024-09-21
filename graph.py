class Graph:
    # Initialize the graph
    def __init__(self):
        self.vertices = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    # Add an edge between two vertices
    def add_edge(self, vertex1, vertex2):
        # Make sure the vertices are in the graph
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        

        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
        else:
            raise ValueError("One or more vertices not in graph")

    # Get the neighbors of a vertex
    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            raise ValueError("Vertex not in graph")

    # Get all vertices in the graph
    def __str__(self):
        return str(self.vertices)
