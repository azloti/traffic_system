from graph import Graph
from priority_queue import PriorityQueue
from graph_utils import find_shortest_path
from hash_table import HashTable

class City:

    def __init__(self):
        self.graph = Graph() # The graph will be used to represent the city
        self.traffic_queue = PriorityQueue() # The priority queue will be used to store traffic at a given node
        self.city_table = HashTable(1000) # The hash table will be used to store the city's nodes