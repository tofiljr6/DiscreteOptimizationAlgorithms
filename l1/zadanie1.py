import argparse
from BFS import BFS
from DFS import DFS

parser = argparse.ArgumentParser()
parser.add_argument('-d', type=bool, nargs='?', help="Directed graph")
parser.add_argument('-f', type=str, nargs='?', help="A source of file where the graphs information is")
parser.add_argument('-t', type=bool, nargs='?', help="Print a edges belong to the bfs/dfs tree")
args = parser.parse_args()

if args.d:
    print("Graph directed")
else:
    print("Graph undirected")

# open file
file = open(file=args.f)

# number of vertexes and edges in tge graph.
# assume that vertex is start counting form 0...n-1
numberOfVertex = int(file.readline())
numberOfEdges = int(file.readline())

# create two graph, one BFS and another one DFS
bfsGraph = BFS(numberOfVertex)
dfsGraph = DFS(numberOfVertex)

# read each edges in the file and add it to the graph neighbourhood's matrix
for edge in range(numberOfEdges):
    line = file.readline().split(' ')
    u, v = int(line[0]), int(line[1].rsplit('\n')[0])

    # if graph is directed
    if args.d:
        bfsGraph.addDirectedEdge(u, v)
        dfsGraph.addDirectedEdge(u, v)
    else:
        bfsGraph.addEdges(u, v)
        dfsGraph.addEdges(u, v)

print("BFS odwiedzone wierzchołki", bfsGraph.bfs())
print("DFS odwiedzone wierzchołki", dfsGraph.dfs())

if args.t:
    print("Drzewo poszukiwań BFS", bfsGraph.printTree())
    print("Drzewo poszukiwań DFS", dfsGraph.dfstree())
