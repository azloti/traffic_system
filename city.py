from graph import Graph
from priority_queue import PriorityQueue
from hash_table import HashTable

class City:

    def __init__(self):
        self.graph = Graph() # The graph will be used to represent the city
        self.city_table = HashTable(10000000) # The hash table will be used to store traffic at a given edge

    def add_edge(self, vertex1, vertex2, traffic):
        # Add the edge to the graph
        self.graph.add_edge(vertex1, vertex2)
        # Add the traffic to the hash table
        self.city_table.insert(f"{vertex1}-{vertex2}", traffic)

    def get_traffic(self, vertex1, vertex2):
        # Get the traffic from the hash table
        return self.city_table.search(f"{vertex1}-{vertex2}")
    
    def find_shortest_path(self, start, end):
        # Check that both vertices are in the graph
        if start not in self.graph.vertices or end not in self.graph.vertices:
            return None

        priority_queue = PriorityQueue()
        priority_queue.enqueue(start, 0)
        visited = set()
        distances = {}
        previous_vertices = {}
        distances[start] = 0

        for vertex in self.graph.vertices:
            if vertex != start:
                distances[vertex] = float("inf")
            previous_vertices[vertex] = None
        
        while not priority_queue.is_empty():
            current_vertex = priority_queue.dequeue()
            visited.add(current_vertex)

            if current_vertex == end:
                break  # Early exit if we reach the destination

            for neighbor in self.graph.get_neighbors(current_vertex):
                if neighbor in visited:
                    continue
                new_path = distances[current_vertex] + self.get_traffic(current_vertex, neighbor)
                if new_path < distances[neighbor]:
                    distances[neighbor] = new_path
                    previous_vertices[neighbor] = current_vertex
                    priority_queue.enqueue(neighbor, distances[neighbor])
        
        path = []
        current_vertex = end
        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]

        
        # Check if the path exists (if start is not the first element in the path, there's no path)
        if not path or path[0] != start:
            return None
        
        return path