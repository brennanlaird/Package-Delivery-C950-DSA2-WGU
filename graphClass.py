'''
This code creates a graph data structure to store the locations and distances imported from the distance table CSV
The original code was taken from Zybooks DSA 2 text, Section 6.6 and modified to improve functionality and readability.
'''


# Define the graph class with a list of adjacent vertexes and list of edge weights.
# The adjacency list will store address IDs as a tuple and the edge weights will represent the distance between vertexes
# represented by the tuple.
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    # Adds a vertex to the adjacency list. The vertex will be represented on the address id pulled from the CSV file.
    # Time Complexity O(1)  Space Complexity O(1)
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    # Directed edge is added between two vertexes and includes an edge weight.
    # Time Complexity O(1)  Space Complexity O(1)
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # Undirected graph edges are added by adding directed edges with the same vertexes and weights  in either order.
    # Time Complexity O(1)  Space Complexity O(1)
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
