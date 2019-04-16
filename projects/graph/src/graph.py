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

    def dft(self, v, visited=set(), output=set()):
        output.add(v)
        for i in self.vertices[v]:
            if i not in visited:
                visited.add(v)
                self.dft(i, visited, output)
        return output

    # def dft_util(self, v, visited):
    #     visited[int(v)] = True
    #     print(v)
    #     for i in self.vertices[v]:
    #         if not visited[int(i)]:
    #             self.dft_util(i, visited)

    # def dft(self, v):
    #     visited = [False]*(len(self.vertices))
    #     return self.dft_util(v, visited)


graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('5', '3')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('7', '1')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('7', '6')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('2', '3')
graph.add_directed_edge('4', '6')
graph.bft('1')
print(graph.dft('1'))
# print(graph.dfs('1'))

# pp = pprint.PrettyPrinter(indent=4)

# pp.pprint(graph.vertices)
