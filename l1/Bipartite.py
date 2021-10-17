from Graph import Graph
from queue import Queue


class Bipartie(Graph):
    def __init__(self, n):
        super().__init__(n)
        self.verticesColor = [-1 for i in range(n)]

    def isBipartie(self, src):
        self.verticesColor[src] = 1

        q = Queue()  # FIFO
        q.put(self.vertices[src])

        while not q.empty():
            u = q.get()

            for v in self.vertices:
                if self.edges[u.id][v.id] == 1 and self.verticesColor[v.id] == -1:
                    self.verticesColor[v.id] = 1 - self.verticesColor[u.id]
                    q.put(v)
                elif self.edges[u.id][v.id] == 1 and self.verticesColor[v.id] == self.verticesColor[u.id]:
                    return False
        return True

    def check(self):
        s = 0
        while not self.isBipartie(s):
            s += 1
            self.verticesColor = [-1 for i in range(self.vertices)]

        return self.isBipartie(s)

    def divide(self):
        # blue = 1
        # red = 0

        blue = []
        red = []

        for i in range(len(self.verticesColor)):
            if self.verticesColor[i] == 1: # blue
                blue.append(i)
            else:
                red.append(i)

        return blue, red