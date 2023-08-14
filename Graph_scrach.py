class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        return []

    def __str__(self):
        return str(self.graph)

# Example usage
if __name__ == "__main__":
    my_graph = Graph()

    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")

    my_graph.add_edge("A", "B")
    my_graph.add_edge("A", "C")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("C", "D")

    print("Graph:")
    print(my_graph)

    print("Neighbors of 'A':", my_graph.get_neighbors("A"))
    print("Neighbors of 'C':", my_graph.get_neighbors("C"))
