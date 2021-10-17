from Node import Node
from Color import Color
from math import inf

class Graph:
    def __init__(self, n):
        self.vertices = [Node(i, Color.WHITE, inf, None) for i in range(n)]
        self.edges = [[None for i in range(n)] for j in range(n)]

    def addEdges(self, u, v, cost=1):
        self.edges[u][v] = cost
        self.edges[v][u] = cost

    def addDirectedEdge(self, u, v, cost=1):
        """
        Add directed edge from u to v with default cost equals 1
        :param u: start vertex
        :param v: end vertex
        :param cost: cost of edges, default = 1
        """
        self.edges[u][v] = cost

    def show(self):
        for e in self.edges:
            print(e)