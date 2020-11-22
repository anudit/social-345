import csv
import numpy as np
from utils import multiply, getTrace, structEdgeList, structEdgeList2, getAlgebraicConnectivity, disperse, getErGraphEdges,getBaGraphEdges, spectralRad, asst, shortPaths
from matplotlib import pyplot as plt

def countFrequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

class Graph:

    def __init__(self, edges):
        self.V = int(np.amax(edges))+1
        self.adj = [[] for i in range(self.V)]
        self.adjMatrix = [[0 for i in range(self.V)] for i in range(self.V)]
        self.edgeList = []
        for ind, row in enumerate(edges):
            self.addEdge(row[0], row[1])

    def addEdge (self, u, v ):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.adjMatrix[u][v] = 1
        self.edgeList.append([u, v])

    def getAdj(self):
        return self.adj[1:]

    def getMatrix(self):
        return self.adjMatrix

    def countEdges(self):
        Sum = 0
        for i in range(self.V):
            Sum += len(self.adj[i])
        return Sum // 2

    def degreeList(self):
        degree = [0 for i in range(self.V + 1)]

        for i in range(len(self.edgeList)):
            degree[self.edgeList[i][0]] += 1
            degree[self.edgeList[i][1]] += 1

        degreeList = []
        for i in range(1, self.V + 1):
            degreeList.append(degree[i])

        return degreeList

    def triangles(self):

        aux2 = multiply(self.adjMatrix, self.adjMatrix)
        aux3 = multiply(self.adjMatrix, aux2)

        trace = getTrace(aux3)
        return trace // 6

    def algebraicConnectivity(self):
        return getAlgebraicConnectivity(self.edgeList)

    def nodeBetweennessCentrality(self):
        print('Calculating Node Betweeness')
        locdata = structEdgeList(self.edgeList)
        locdata = list(locdata.items())
        x = []
        y = []
        for ind, tup in enumerate(locdata):
            x.append(tup[0])
            y.append(tup[1])
        return [x, y]

    def edgeBetweennessCentrality(self):
        print('Calculating Edge Betweeness')
        locdata = structEdgeList2(self.edgeList)
        locdata = list(locdata.items())
        x = []
        y = []
        for ind, tup in enumerate(locdata):
            x.append(ind)
            y.append(tup[1])
        return [x, y]

    def dispersion(self):
        locdata = structEdgeList2(self.edgeList)
        locdata = list(locdata.items())
        x = []
        y = []
        for ind, tup in enumerate(locdata):
            x.append(ind)
            y.append(tup[1])
        return [x, y]

    def dispersion(self):
        print('Calculating Dispersion')
        locdata = disperse(self.edgeList)
        locdata = list(locdata.items())
        x = []
        y = []
        for ind, tup in enumerate(locdata):
            x.append(tup[0])
            stdev = np.std(list(tup[1].values()))
            y.append(stdev)
        return [x, y]

    def degreeDistribution(self):
        deg_list = self.degreeList()
        fr = countFrequency(deg_list).items()
        x = []
        y = []
        for ind, tup in enumerate(fr):
            x.append(tup[0])
            y.append(tup[1])
        return [x, y]

    def spec(self):
        locdata = spectralRad(self.edgeList)
        x = []
        y = []
        for ind, val in enumerate(locdata):
            x.append(ind)
            y.append(val)
        return [x, y]

    def assortativity(self):
        return asst(self.edgeList)

    def probDist(self):
        cnts = [0 for _ in range(self.V+1)]

        for i in range(1, self.V+1):
            shp = shortPaths(self.edgeList, i)
            for key, value in shp.items():
                cnts[i]+=len(value)

        print(cnts)
        # dl = self.degreeList()

        # # group by degree
        # gr = [[] for x in range(self.V+1)]
        # for ind, val in enumerate(dl):
        #     gr[val].append(ind)
        # print(len(gr))
        # print(gr)


def getData(name = ''):
    db = []
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            db.append([int(x) for x in row[:2]])
    return np.array(db)

# Load from CSV
DS_NAME = '15.csv'
data = getData(DS_NAME)
g = Graph(data)

# Load ER Graph
data_er = getErGraphEdges(g.V, 0.5)
g_er = Graph(data_er)

# # Load BA Graph
data_ba = getBaGraphEdges(g.V, 10)
g_ba = Graph(data_ba)


print(g.countEdges())
print(np.average(g.degreeList()))
print(np.max(g.degreeList()))
print(g.triangles())
print(g.algebraicConnectivity())

Node Betweeness
g_cent_data = g.nodeBetweennessCentrality()
g_er_cent_data = g_er.nodeBetweennessCentrality()
g_ba_cent_data = g_ba.nodeBetweennessCentrality()
plt.xlabel('Nodes')
plt.ylabel('Node Betweeness')
plt.scatter(g_cent_data[0],g_cent_data[1], s=20, label=f"Dataset {DS_NAME}")
plt.scatter(g_er_cent_data[0],g_er_cent_data[1], marker='x', s=20, label='Equivalent ER Model')
plt.scatter(g_ba_cent_data[0],g_ba_cent_data[1], marker='*', s=20, label='Equivalent BA Model')
plt.yscale('log')
plt.legend()
plt.show()

Edge Betweeness
g_cent_data = g.edgeBetweennessCentrality()
g_er_cent_data = g_er.edgeBetweennessCentrality()
g_ba_cent_data = g_ba.edgeBetweennessCentrality()
plt.xlabel('Edges')
plt.ylabel('Edge Betweeness')
plt.scatter(g_cent_data[0],g_cent_data[1], s=20, label=f"Dataset {DS_NAME}")
plt.scatter(g_er_cent_data[0],g_er_cent_data[1], marker='x', s=20, label='Equivalent ER Model')
plt.scatter(g_ba_cent_data[0],g_ba_cent_data[1], marker='*', s=20, label='Equivalent BA Model')
plt.yscale('log')
plt.legend()
plt.show()


Calculating Dispersion
deg_dist = g.degreeList()
er_deg_dist = g_er.degreeList()
ba_deg_dist = g_ba.degreeList()
plt.errorbar(
    [x for x in range(1, len(deg_dist)+1)], deg_dist,
    yerr = [x*0.2 for x in deg_dist],
    fmt='o',
    label=f"Dataset {DS_NAME}")
plt.errorbar(
    [x for x in range(1, len(er_deg_dist)+1)], er_deg_dist,
    yerr = [x*0.1 for x in er_deg_dist],
    fmt='x',
    label='Equivalent ER Model')
plt.errorbar(
    [x for x in range(1, len(ba_deg_dist)+1)], ba_deg_dist,
    yerr = [x*0.1 for x in ba_deg_dist],
    fmt='*',
    label='Equivalent BA Model')
plt.xlabel('Nodes')
plt.ylabel('Count')
plt.yscale('log')
plt.legend()
plt.show()

print('Calculating Degree Distribution')
deg_dist = g.degreeDistribution()
plt.scatter(deg_dist[0],deg_dist[1])
plt.xlabel('Degree')
plt.ylabel('Count')
plt.show()

print('Calculating Spectral Radius')
spec_data = g.spec()
plt.scatter(spec_data[0],spec_data[1])
plt.show()

print(g.assortativity())


g.probDist()
