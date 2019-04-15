import pprint
from collections import deque
"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[str(vertex)] = set()

    def add_edge(self, vertex_a, vertex_b):
        if vertex_a in self.vertices and vertex_b in self.vertices:
            self.add_directed_edge(vertex_a, vertex_b)
            self.add_directed_edge(vertex_b, vertex_a)
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, vertex_a, vertex_b):
        if vertex_a in self.vertices and vertex_b in self.vertices:
            self.vertices[str(vertex_a)].add(str(vertex_b))

    def bft(self, start):
        queue = deque([start])
        visited = set()
        while len(queue) > 0:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                for i in self.vertices[vertex]:
                    queue.append(i)
        print(visited)

    def dft(self, start):
        stack = [start]
        visited = set()
        while len(stack) > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                for i in self.vertices[vertex]:
                    stack.append(i)
        print(visited)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.bft('0')
graph.dft('0')

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(graph.vertices)
