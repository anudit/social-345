import networkx as codebase
from numba import jit

@jit(nopython=True)
def multiply(A, B):
    V = len(A)
    res = [[0 for i in range(len(A))] for i in range(len(A))]
    for i in range(V):
        for j in range(V):
            res[i][j] = 0
            for k in range(V):
                res[i][j] += A[i][k] * B[k][j]
    return res

def getTrace(graph):
    trace = 0
    V = len(graph)
    for i in range(V):
        trace += graph[i][i]
    return trace

def getAlgebraicConnectivity(edgeList):
    G = codebase.Graph()
    for ind, row in enumerate(edgeList):
        G.add_edge(row[0], row[1])
    return codebase.algebraic_connectivity(G)

# getBetweennessCentrality
def structEdgeList(edgeList):
    G = codebase.Graph()
    for ind, row in enumerate(edgeList):
        G.add_edge(row[0], row[1])
    return codebase.betweenness_centrality(G)

# getEdgeBetweennessCentrality
def structEdgeList2(edgeList):
    G = codebase.Graph()
    for ind, row in enumerate(edgeList):
        G.add_edge(row[0], row[1])
    return codebase.algorithms.centrality.edge_betweenness_centrality(G)

def disperse(edgeList):
    G = codebase.Graph()
    for ind, row in enumerate(edgeList):
        G.add_edge(row[0], row[1])
    return codebase.dispersion(G)

def getErGraphEdges(nodes = 0, prob = 0):
    G= codebase.erdos_renyi_graph(nodes,prob)
    # A = codebase.to_numpy_matrix(G)
    el = [[int(x.split(' ')[0]), int( x.split(' ')[1])] for x in codebase.generate_edgelist(G, data=False)]
    return el

def getBaGraphEdges(nodes = 0, edges = 0):
    G= codebase.barabasi_albert_graph(n=nodes, m=edges)
    # A = codebase.to_numpy_matrix(G)
    el = [[int(x.split(' ')[0]), int( x.split(' ')[1])] for x in codebase.generate_edgelist(G, data=False)]
    return el

def spectralRad(edgeList):
    G = codebase.Graph()
    for ind, row in enumerate(edgeList):
        G.add_edge(row[0], row[1])
    return codebase.linalg.spectrum.laplacian_spectrum(G)

def asst(edgeList):
    G = codebase.Graph()
    for ind, row in enumerate(edgeList):
        G.add_edge(row[0], row[1])
    return codebase.degree_assortativity_coefficient(G)

def shortPaths(edgeList, cap):
    G = codebase.Graph()
    for ind, row in enumerate(edgeList):
        G.add_edge(row[0], row[1])
    return dict(codebase.all_pairs_shortest_path(G, cap))

