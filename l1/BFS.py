import math
from Color import Color
from queue import Queue
from Graph import Graph


class BFS(Graph):
    """
    The class represent the graph using bfs algorithm
    """

    def __init__(self, n):
        super().__init__(n)
        self.tree = []  # an array of edge represents bfs tree

    def bfs(self, s=0):
        """
        :param s: starting vertex, default is 0
        :return: the array in order vertex has been visited
        """
        vertexVisit = []  # an array of vertex visited in order

        for u in self.vertices:
            if u != self.vertices[s]:
                u.color = Color.WHITE
                u.d = math.inf
                u.pi = None

        self.vertices[s].color = Color.GRAY
        self.vertices[s].d = 0
        self.vertices[s].pi = None

        Q = Queue()
        Q.put(self.vertices[s])

        while not Q.empty():
            u = Q.get()
            vertexVisit.append(u.id)
            # print("GET:", u.id)
            for v in range(len(self.edges[u.id])):
                if self.edges[u.id][v] is not None:
                    if self.vertices[v].color == Color.WHITE:
                        self.vertices[v].color = Color.GRAY
                        self.vertices[v].d = self.vertices[u.id].d + 1
                        self.vertices[v].pi = u

                        Q.put(self.vertices[v])

                        self.tree.append([u.id, v])
            u.color = Color.BLACK
        return vertexVisit

    def printTree(self):
        """
        The method return the array with edges belong to bfs tree.
        Before run the method, must bfs method runs. Otherwise returns incorrect data
        :return: edges belong to bfs tree.
        """
        return self.tree
