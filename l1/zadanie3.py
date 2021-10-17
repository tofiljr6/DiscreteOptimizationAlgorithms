import argparse
from DFS import DFS

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, nargs='?', help="A source of file where the graphs information is")
args = parser.parse_args()

file = open(args.f)

# number of vertexes and edges in tge graph.
# assume that vertex is start counting form 0...n-1
numberOfVertex = int(file.readline())
numberOfEdges = int(file.readline())

dfsGraph = DFS(numberOfVertex)

for edge in range(numberOfEdges):
    line = file.readline().split(' ')
    u, v = int(line[0]), int(line[1].rsplit('\n')[0])

    dfsGraph.addDirectedEdge(u, v)

dfsGraph.sccs()