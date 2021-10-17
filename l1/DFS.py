import collections
from Graph import Graph
from Color import Color


class DFS(Graph):
    def __init__(self, n):
        super().__init__(n)
        self.time = 0
        self.vertexVisit = []
        self.dfsTreeEdges = []
        self.topology = collections.deque()
        self.topologyArray = []
        self.edgesT = []
        self.dfste = []

    def dfs(self):
        """

        :return:  The method returns the array of vertex have been visited
        """
        for u in self.vertices:
            u.color = Color.WHITE
            u.pi = None

        self.time = 0

        for u in self.vertices:
            if u.color == Color.WHITE:
                self.vertexVisit.append(u.id)
                self.dfsVisit(u)

        return self.vertexVisit

        # for v in self.vertices:
        #     b = False
        #     for t in self.dfsTreeEdges:
        #         if t[0] == v.id or t[1] == v.id:
        #             b = True
        #     if not b:
        #         self.dfsTreeEdges.append(v.id)

    def dfsVisit(self, u, doTopology=False):
        self.time += 1  # white vertex u has just been discovered

        # todo  - dirty code  - fix them later
        for i in self.vertices:
            if i.id == u:
                u = i

        u.d = self.time
        u.color = Color.GRAY
        for v in self.vertices:  # explore edge (u, v)
            if self.edges[u.id][v.id] is not None:
                if v.color == Color.WHITE:
                    v.pi = u
                    self.dfsTreeEdges.append([u.id, v.id])  # add edge to array of edges belong to dfs tree
                    self.vertexVisit.append(v.id)
                    self.dfsVisit(v, doTopology)

        u.color = Color.BLACK  # blacken u; it is finished
        self.time += 1
        u.f = self.time

        if doTopology:
            self.topology.insert(0, u)

    def dfstree(self):
        """
        The method returns the array with edges which belong to dfs tree
        :return: array
        """
        return self.dfsTreeEdges

    def topologySort(self):
        """
        The method pritn vertex in topology sort, using dfs algorithms.
        :return: array
        """
        for u in self.vertices:
            u.color = Color.WHITE
            u.pi = None

        self.time = 0

        for u in self.vertices:
            if u.color == Color.WHITE:
                self.vertexVisit.append(u.id)
                self.dfsVisit(u, True)

        return self.topology

    def topologySortPrint(self):
        print("Wierzchołki w porządku topologicznym:  ", end="")
        for i in self.topology:
            print(i.id, end=" ")
            self.topologyArray.append(i.id)

        print("\n")

        # cycle - be or not to be
        cycle = False
        # print("topologyarray", self.topologyArray)

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.edges[i][j] is not None:
                    if self.topologyArray.index(i) > self.topologyArray.index(j):
                        cycle = True

        print("CYCLE:", cycle)

    def transition(self):
        """
        The time complexity is not good. Is better algorithms? O(n^2)
        :return: returns martix's transition
        """
        edgesTrans = [[None for i in range(len(self.vertices))] for j in range(len(self.vertices))]

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.edges[i][j] is not None:
                    edgesTrans[j][i] = self.edges[i][j]

        # for edge in edgesTrans:
        #     print(edge)

        return edgesTrans

    def prepost(self):
        for i in self.vertices:
            print(i.id, " ", i.d, " ", i.f, " ", i.pi)

    def sccs(self):
        # step 0 - reset all variables
        self.dfsTreeEdges = []

        # step 1 - call dfs to compute finishing times u.f for each vertex u
        self.dfs()
        self.dfsTreeEdges = []

        # step 2 - compute G^T
        self.edgesT = self.transition()

        # step 3 - call dfs G^T but in the main loop of DFS, consider the vertices in order of decreasing u.f

        # step 3.1 - the vertices in order of decreasing u.f
        self.vertices.sort(key=lambda node: node.f, reverse=True)

        for u in self.vertices:
            u.color = Color.WHITE
            u.pi = None

        self.time = 0

        for u in self.vertices:
            if u.color == Color.WHITE:
                self.vertexVisit.append(u.id)
                self.dfsVisit2(u)

            if len(self.dfste) != 0:
                self.dfsTreeEdges.append(self.dfste)
                self.dfste = []
            # print(self.dfsTreeEdges)

        # printing
        vertexinsccs = []
        for s in self.dfsTreeEdges:
            for e in s:
                vertexinsccs.append(e[0])
                vertexinsccs.append(e[1])

        print(vertexinsccs)

        for i in range(len(self.vertices)):
            if vertexinsccs.count(i) == 0:
                self.dfsTreeEdges.append(i)

        for i in range(len(self.dfsTreeEdges)):
            print("Do", i, "składowej należa krawędzie",  self.dfsTreeEdges[i])

    def dfsVisit2(self, u):
        self.time += 1  # white vertex u has just been discovered

        for i in self.vertices:
            if i.id == u:
                u = i

        u.d = self.time
        u.color = Color.GRAY
        for v in self.vertices: # explore edge (u,v)
            if self.edgesT[u.id][v.id] is not None:
                if v.color == Color.WHITE:
                    v.pi = u
                    self.dfste.append([v.id, u.id])
                    self.vertexVisit.append(v.id)
                    self.dfsVisit2(v)

        u.color = Color.BLACK
        self.time += 1
        u.f = self.time

